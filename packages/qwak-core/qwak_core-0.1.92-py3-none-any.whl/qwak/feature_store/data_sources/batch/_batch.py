from abc import abstractmethod
from dataclasses import dataclass

from _qwak_proto.qwak.feature_store.sources.batch_pb2 import (
    BatchSource as ProtoBatchSource,
)
from qwak.feature_store.data_sources.base import BaseSource


@dataclass
class BaseBatchSource(BaseSource):
    date_created_column: str

    @abstractmethod
    def _to_proto(self) -> ProtoBatchSource:
        pass

    @classmethod
    @abstractmethod
    def _from_proto(cls, proto):
        pass
