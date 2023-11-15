import ast
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Optional

from _qwak_proto.qwak.feature_store.entities.entity_pb2 import (
    EntityDefinition,
    EntitySpec,
)
from _qwak_proto.qwak.feature_store.features.feature_set_pb2 import FeatureSetSpec
from _qwak_proto.qwak.features_operator.v3.features_operator_async_service_pb2 import (
    FeatureSetValidationOptions as ProtoFeatureSetValidationOptions,
)
from qwak.feature_store._common.feature_set_utils import generate_key_unique_name
from qwak.feature_store.entities.entity import Entity

if TYPE_CHECKING:
    try:
        import pandas as pd
    except ImportError:
        pass

from _qwak_proto.qwak.features_operator.v3.features_operator_pb2 import (
    ValidationSuccessResponse,
)
from qwak.clients.feature_store import FeatureRegistryClient
from qwak.clients.feature_store.operator_client import FeaturesOperatorClient
from qwak.exceptions import QwakException
from qwak.feature_store._common.functions import print_validation_outputs
from qwak.feature_store.validation_options import FeatureSetValidationOptions


@dataclass
class BaseFeatureSet(ABC):
    name: str
    data_sources: List[str]
    entity: str = None
    key: str = None

    def _get_entity_definition(
        self, feature_registry: FeatureRegistryClient
    ) -> EntityDefinition:
        # fs has a key def but not an entity def, return an entity that is valid but not registered
        # This is done mainly for the validation flow/get sample, to avoid registering temporary entities for keys
        if self.key and not self.entity:
            new_key_name: str = generate_key_unique_name(self.name)

            new_key_spec: EntitySpec = Entity(
                name=new_key_name,
                description=f"Key of feature set {self.name}",
                key=self.key,
            )._to_proto()

            # return new entity def with no id
            entity_definition: EntityDefinition = EntityDefinition(
                entity_spec=new_key_spec
            )
        else:
            feature_set_entity = feature_registry.get_entity_by_name(self.entity)

            if not feature_set_entity:
                raise QwakException(
                    f"Trying to register a feature set with a non existing entity or bad key configuration-: {self.entity}"
                )

            entity_definition: EntityDefinition = (
                feature_set_entity.entity.entity_definition
            )

        return entity_definition

    @staticmethod
    @abstractmethod
    def _from_proto(cls, proto: FeatureSetSpec):
        pass

    @abstractmethod
    def _to_proto(
        self,
        git_commit,
        features,
        feature_registry,
        **kwargs,
    ) -> FeatureSetSpec:
        pass

    def get_sample(
        self,
        number_of_rows: int = 10,
        validation_options: Optional[FeatureSetValidationOptions] = None,
    ) -> "pd.DataFrame":
        """
        Fetches a sample of the Feature set transformation by loading requested sample of data from the data source
        and executing the transformation on that data.

        :param number_of_rows: number of rows requests
        :param validation_options: validation options
        :returns Sample Pandas Dataframe

        Example:

        ... code-block:: python
            @batch.feature_set(entity="users", data_sources=["snowflake_users_table"])
            @batch.backfill(start_date=datetime(2022, 1, 1))
            def user_features():
                return SparkSqlTransformation("SELECT user_id, age FROM data_source")

            sample_features = user_features.get_sample()
            print(sample_feature)
            #	    user_id	         timestamp	        user_features.age
            # 0	      1	        2021-01-02 17:00:00	              23
            # 1	      1	        2021-01-01 12:00:00	              51
            # 2	      2	        2021-01-02 12:00:00	              66
            # 3	      2	        2021-01-01 18:00:00	              34
        """

        try:
            import pandas as pd
        except ImportError:
            raise QwakException("Missing Pandas dependency required for getting sample")

        if 0 >= number_of_rows > 1000:
            raise ValueError(
                f"`number_rows` must be under 1000 and positive, got: {number_of_rows}"
            )

        operator_client = FeaturesOperatorClient()
        registry_client = FeatureRegistryClient()

        featureset_spec = self._to_proto(
            git_commit=None, features=None, feature_registry=registry_client
        )
        validation_options_proto: Optional[ProtoFeatureSetValidationOptions] = (
            validation_options.to_proto() if validation_options else None
        )

        result = operator_client.validate_featureset_blocking(
            featureset_spec=featureset_spec,
            resource_path=None,
            num_samples=number_of_rows,
            validation_options=validation_options_proto,
        )

        response = getattr(result, result.WhichOneof("type"))
        if isinstance(response, ValidationSuccessResponse):
            print_validation_outputs(response)

            return pd.read_json(
                path_or_buf=ast.literal_eval(response.sample),
                dtype=response.spark_column_description,
            )
        else:
            raise QwakException(f"Sampling failed:\n{response}")
