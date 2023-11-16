from abc import abstractmethod
from typing import Optional
from uuid import UUID

from lqs.interface.base.delete import DeleteInterface as BaseDeleteInterface


class DeleteInterface(BaseDeleteInterface):
    @abstractmethod
    def _digestion(self, **kwargs):
        pass

    def digestion(self, digestion_id: UUID):
        return self._digestion(
            digestion_id=digestion_id,
        )

    @abstractmethod
    def _digestion_part(self, **kwargs):
        pass

    def digestion_part(
        self, digestion_part_id: UUID, digestion_id: Optional[UUID] = None
    ):
        return self._digestion_part(
            digestion_part_id=digestion_part_id,
            digestion_id=digestion_id,
        )

    @abstractmethod
    def _digestion_topic(self, **kwargs):
        pass

    def digestion_topic(
        self, digestion_topic_id: UUID, digestion_id: Optional[UUID] = None
    ):
        return self._digestion_topic(
            digestion_topic_id=digestion_topic_id,
            digestion_id=digestion_id,
        )

    @abstractmethod
    def _group(self, **kwargs):
        pass

    def group(self, group_id: UUID):
        return self._group(
            group_id=group_id,
        )

    @abstractmethod
    def _hook(self, **kwargs):
        pass

    def hook(self, hook_id: UUID, workflow_id: Optional[UUID] = None):
        return self._hook(
            hook_id=hook_id,
            workflow_id=workflow_id,
        )

    @abstractmethod
    def _ingestion(self, **kwargs):
        pass

    def ingestion(self, ingestion_id: UUID):
        return self._ingestion(
            ingestion_id=ingestion_id,
        )

    @abstractmethod
    def _ingestion_part(self, **kwargs):
        pass

    def ingestion_part(self, ingestion_part_id: UUID, ingestion_id: Optional[UUID]):
        return self._ingestion_part(
            ingestion_part_id=ingestion_part_id,
            ingestion_id=ingestion_id,
        )

    @abstractmethod
    def _label(self, **kwargs):
        pass

    def label(self, label_id: UUID):
        return self._label(
            label_id=label_id,
        )

    @abstractmethod
    def _log(self, **kwargs):
        pass

    def log(self, log_id: UUID):
        return self._log(
            log_id=log_id,
        )

    @abstractmethod
    def _log_object(self, **kwargs):
        pass

    def log_object(self, log_id: UUID, object_key: str):
        return self._log_object(
            log_id=log_id,
            object_key=object_key,
        )

    @abstractmethod
    def _object(self, **kwargs):
        pass

    def object(self, object_store_id: UUID, object_key: str):
        return self._object(
            object_store_id=object_store_id,
            object_key=object_key,
        )

    @abstractmethod
    def _object_store(self, **kwargs):
        pass

    def object_store(self, object_store_id: UUID):
        return self._object_store(
            object_store_id=object_store_id,
        )

    @abstractmethod
    def _query(self, **kwargs):
        pass

    def query(self, query_id: UUID, log_id: Optional[UUID] = None):
        return self._query(
            query_id=query_id,
            log_id=log_id,
        )

    @abstractmethod
    def _record(self, **kwargs):
        pass

    def record(self, timestamp: float, topic_id: UUID):
        return self._record(
            timestamp=timestamp,
            topic_id=topic_id,
        )

    @abstractmethod
    def _tag(self, **kwargs):
        pass

    def tag(self, tag_id: UUID, log_id: Optional[UUID] = None):
        return self._tag(
            tag_id=tag_id,
            log_id=log_id,
        )

    @abstractmethod
    def _topic(self, **kwargs):
        pass

    def topic(self, topic_id: UUID):
        return self._topic(
            topic_id=topic_id,
        )

    @abstractmethod
    def _workflow(self, **kwargs):
        pass

    def workflow(self, workflow_id: UUID):
        return self._workflow(
            workflow_id=workflow_id,
        )
