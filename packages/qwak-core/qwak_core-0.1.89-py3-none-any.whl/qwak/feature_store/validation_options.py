from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from _qwak_proto.qwak.features_operator.v3.features_operator_async_service_pb2 import (
    DataSourceValidationOptions as ProtoDataSourceValidationOptions,
    FeatureSetValidationOptions as ProtoFeatureSetValidationOptions,
    ValidationTimeRange as ProtoValidationTimeRange,
)
from google.protobuf.timestamp_pb2 import Timestamp as ProtoTimestamp
from qwak.utils.datetime_utils import datetime_to_pts


@dataclass
class ValidationTimeRange:
    lower_time_bound: Optional[datetime] = None
    upper_time_bound: Optional[datetime] = None

    def to_proto(self) -> ProtoValidationTimeRange:
        lower_time_bound_proto: Optional[ProtoTimestamp] = None
        upper_time_bound_proto: Optional[ProtoTimestamp] = None

        if self.lower_time_bound:
            lower_time_bound_proto = datetime_to_pts(self.lower_time_bound)
        if self.upper_time_bound:
            upper_time_bound_proto = datetime_to_pts(self.upper_time_bound)

        return ProtoValidationTimeRange(
            lower_time_bound=lower_time_bound_proto,
            upper_time_bound=upper_time_bound_proto,
        )


@dataclass
class DataSourceValidationOptions(ValidationTimeRange):
    def to_proto(self) -> ProtoDataSourceValidationOptions:
        validation_time_range_proto = (
            super().to_proto()
            if self.lower_time_bound or self.upper_time_bound
            else None
        )

        return ProtoDataSourceValidationOptions(
            validation_time_range=validation_time_range_proto
        )


@dataclass
class FeatureSetValidationOptions(ValidationTimeRange):
    data_source_limit: Optional[int] = None

    def to_proto(self) -> ProtoFeatureSetValidationOptions:
        validation_time_range_proto = (
            super().to_proto()
            if self.lower_time_bound or self.upper_time_bound
            else None
        )

        return ProtoFeatureSetValidationOptions(
            data_source_limit=self.data_source_limit,
            validation_time_range=validation_time_range_proto,
        )
