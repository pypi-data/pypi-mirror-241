import logging
import os
from distutils.util import strtobool
from typing import TYPE_CHECKING, List, Optional

import grpc
from _qwak_proto.qwak.ecosystem.v0.ecosystem_pb2 import AuthenticatedUnifiedUserContext
from _qwak_proto.qwak.feature_store.serving.serving_pb2 import (
    BatchFeature as ServingProtoBatchFeature,
    BatchV1Feature as ServingProtoBatchV1Feature,
    EntitiesHeader,
    EntityToFeatures,
    EntityValueRow,
    Feature as ServingProtoFeature,
    RequestedEntitiesMatrix,
    RequestedEntitiesMatrixRequest,
    RequestMetaData,
)
from _qwak_proto.qwak.feature_store.serving.serving_pb2_grpc import ServingServiceStub
from qwak.clients.administration.eco_system.client import EcosystemClient
from qwak.exceptions import QwakException
from qwak.feature_store._common.feature_set_utils import BatchFeature, BatchFeatureV1
from qwak.inner.tool.grpc.grpc_tools import create_grpc_channel
from qwak.model.schema import ModelSchema
from qwak.model.schema_entities import BaseFeature, RequestInput

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    try:
        import pandas as pd
    except ImportError:
        pass

_ONLINE_SERVING_ENDPOINT_OVERRIDE_ENV_VAR = "ONLINE_SERVING_ENDPOINT"  # nosec B105
_ONLINE_SERVING_SSL_OVERRIDE_ENV_VAR = "ONLINE_SERVING_FORCE_SSL"  # nosec B105
_ONLINE_SERVING_TOKEN_HEADER_ENV_VAR = "ONLINE_SERVING_TOKEN_HEADER"  # nosec B105


class OnlineClient:
    """
    Online Feature Serving client
    """

    def __init__(
        self,
        enable_ssl: bool = False,
        endpoint_url: Optional[str] = None,
    ):
        default_endpoint_url: str = "fs-serving-webapp.qwak.svc.cluster.local:6577"

        options = (
            ("grpc.keepalive_timeout_ms", 1500),
            ("grpc.client_idle_timeout_ms", 60 * 1000),
        )

        user_context: AuthenticatedUnifiedUserContext = (
            EcosystemClient().get_authenticated_user_context().user
        )

        if endpoint_url is None:
            # running from a pod inside k8s cluster
            if "K8S_POD_NAME" in os.environ:
                endpoint_url = os.environ.get(
                    _ONLINE_SERVING_ENDPOINT_OVERRIDE_ENV_VAR, default_endpoint_url
                )
                enable_ssl = False
            else:
                environment_id: str = (
                    user_context.account_details.default_environment_id
                )
                endpoint_url: str = user_context.account_details.environment_by_id[
                    environment_id
                ].configuration.edge_services_url
                enable_ssl = True

        enable_ssl = bool(
            strtobool(
                os.environ.get(_ONLINE_SERVING_SSL_OVERRIDE_ENV_VAR, str(enable_ssl))
            )
        )

        force_token_header: bool = bool(
            strtobool(os.environ.get(_ONLINE_SERVING_TOKEN_HEADER_ENV_VAR, str(True)))
        )

        # As of time of writing, feature-store is single env!
        self._metadata = (
            ("qwak-user-id", user_context.user_id),
            ("qwak-account-id", user_context.account_details.id),
            (
                "qwak-environment-id",
                user_context.account_details.default_environment_id,
            ),
        )

        logger.info(
            f"Online Store network config: "
            f"ssl: {enable_ssl}."
            f"token header: {force_token_header}."
            f"endpoint: {endpoint_url}"
        )

        channel = create_grpc_channel(
            url=endpoint_url,
            enable_ssl=enable_ssl,
            options=options,
            status_for_retry=(
                grpc.StatusCode.UNAVAILABLE,
                grpc.StatusCode.DEADLINE_EXCEEDED,
                grpc.StatusCode.UNAUTHENTICATED,
            ),
            force_token_header=force_token_header,
        )

        self._serving_client: ServingServiceStub = ServingServiceStub(channel)

    @staticmethod
    def to_string_entities_values(values) -> List[str]:
        return [str(value) for value in values]

    def get_feature_values(
        self, schema: ModelSchema, df: "pd.DataFrame", model_name: str = "no-model"
    ) -> "pd.DataFrame":
        """
        :param schema: a ModelSchema object - defines the entities, features and prediction (irelevant in this case).
        :param df: a pandas data-frame with a column for each explicit feature needed
                         and a column for each entity key defined in the schema.
        :return: a pandas data-frame - the feature values defined in the schema
                                       of the requested entities in the df.

        each row in the returned data-frame is constructed by retrieving the most recent requested feature values
        of the entity key(s) for the specific entity value(s) defined in the df.

        TODO: fix imports and align example
        Examples:
        >>> import pandas as pd
        >>> from qwak.feature_store import OnlineClient
        >>> from qwak.model.schema import (
        >>>     ModelSchema, FeatureStoreInput
        >>> )
        >>>
        >>> user_id = Entity(name='uuid', type=str)
        >>>
        >>> model_schema = ModelSchema(
        >>>     entities=[
        >>>         user_id
        >>>     ],
        >>>     inputs=[
        >>>         FeatureStoreInput(entity=user_id, name='user_purchases.number_of_purchases'),
        >>>         FeatureStoreInput(entity=user_id, name='user_purchases.avg_purchase_amount'),
        >>>     ],
        >>>     outputs=[
        >>>         InferenceOutput(name="score", type=float)
        >>>     ])
        >>>
        >>> online_client = OnlineClient()
        >>>
        >>> df = pd.DataFrame(columns=  ['uuid', 'explicit_feature_purchase_price'],
        >>>                   data   =  [ '1'  ,                22                ])
        >>>
        >>> user_features = online_client.get_feature_values(
        >>>                     model_schema,
        >>>                     df)
        >>>
        >>> print(user_features.head())
        >>>	#       user_purchases.number_of_purchases	user_purchases.avg_purchase_amount    otf_quad_price
        >>> # 0	                    76	                              4.796842                     484
        """
        try:
            import pandas as pd
        except ImportError:
            raise QwakException(
                "Missing Pandas dependency required for querying the online feature store"
            )

        (
            entity_features_compounds,
            entities_with_index,
            feature_set_names,
        ) = self._create_entity_and_features_sets(
            schema, pd.DataFrame(df.iloc[0]).transpose()
        )

        if not entity_features_compounds:
            df_result = pd.DataFrame(
                columns=[
                    input_field.name
                    for input_field in schema._inputs
                    if isinstance(input_field, BaseFeature)
                ]
            )

            return pd.concat([df, df_result], axis=1, join="inner")

        entities_to_features = []
        number_of_keys_to_extract = 0
        for entity_features_compound in entity_features_compounds.values():
            number_of_keys_to_extract += len(entity_features_compound.features)
            entities_to_features.append(
                EntityToFeatures(
                    features=entity_features_compound.features,
                    entity_name=entity_features_compound.entity_name,
                )
            )

        ordered_entities_tuple = sorted(
            entities_with_index, key=lambda entity: entity[1]
        )
        ordered_entities = [entity[0] for entity in ordered_entities_tuple]
        entities_values = df[ordered_entities].values.tolist()

        entities_values_req = []
        for index, values in enumerate(entities_values):
            list_of_string_values = self.to_string_entities_values(values)
            entities_values_req.append(
                EntityValueRow(index=index, entity_values=list_of_string_values)
            )

        requested_entities_matrix = RequestedEntitiesMatrix(
            header=EntitiesHeader(entity_names=ordered_entities),
            rows=entities_values_req,
        )

        feature_value_requests = RequestedEntitiesMatrixRequest(
            entity_values_matrix=requested_entities_matrix,
            entities_to_features=entities_to_features,
            request_meta_data=RequestMetaData(
                model_name=model_name,
                feature_set_names=list(feature_set_names),
                num_keys=number_of_keys_to_extract,
            ),
        )

        try:
            response_df_json, _ = self._serving_client.GetMultiFeatures.with_call(
                feature_value_requests, metadata=self._metadata
            )
            result_df = pd.read_json(response_df_json.pandas_df_as_json, orient="split")
            return pd.concat(
                [df.reset_index(drop=True), result_df], axis=1, join="inner"
            )
        except Exception as e:
            raise QwakException(f"Failed to get online features results. Error is: {e}")

    @staticmethod
    def _create_entity_and_features_sets(schema: ModelSchema, df: "pd.DataFrame"):
        entity_features_compounds = {}
        list_of_df_columns = df.columns.to_list()
        entities_and_indexes = []
        feature_set_names = set()
        for entity in schema._entities:
            if entity.name not in df:
                logger.error(
                    f"Schema entity key '{entity.name}' does not exist in the request DataFrame"
                )
            else:
                entity_features_compounds[entity.name] = EntityFeaturesCompound(
                    entity.name, df[entity.name]
                )
                entities_and_indexes.append(
                    (entity.name, list_of_df_columns.index(entity.name))
                )

        for feature in [
            feature
            for feature in schema._inputs
            if not isinstance(feature, RequestInput)
        ]:
            if feature.entity.name not in entity_features_compounds:
                logger.info(
                    f"The entity: {feature.entity.name} of the Feature: {feature} does not exist in the entities list"
                )

            else:
                if isinstance(feature, BatchFeatureV1):
                    feature_proto = ServingProtoFeature(
                        batch_v1_feature=ServingProtoBatchV1Feature(name=feature.name)
                    )
                elif isinstance(feature, BatchFeature):
                    feature_proto = ServingProtoFeature(
                        batch_feature=ServingProtoBatchFeature(name=feature.name)
                    )
                else:
                    raise ValueError(
                        f"Not support type for feature extraction - {type(feature)}"
                    )

                entity_features_compounds[feature.entity.name].add_feature(
                    feature_proto
                )
                feature_set_names.add(feature.name.split(".")[0])

        return entity_features_compounds, entities_and_indexes, feature_set_names


class EntityFeaturesCompound:
    def __init__(self, entity_name, entity_value):
        self.entity_name = entity_name
        self.entity_value = entity_value
        self.features = []

    def add_feature(self, feature):
        self.features.append(feature)
