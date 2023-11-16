from abc import abstractmethod
from typing import Optional
from uuid import UUID

from lqs.interface.base.fetch import FetchInterface as BaseFetchInterface
import lqs.interface.core.models as models


class FetchInterface(BaseFetchInterface):
    @abstractmethod
    def _digestion(self, **kwargs) -> models.DigestionDataResponse:
        pass

    def digestion(self, digestion_id: UUID):
        return self._digestion(
            digestion_id=digestion_id,
        )

    @abstractmethod
    def _digestion_part(self, **kwargs) -> models.DigestionPartDataResponse:
        pass

    def digestion_part(
        self, digestion_part_id: UUID, digestion_id: Optional[UUID] = None
    ):
        return self._digestion_part(
            digestion_id=digestion_id,
            digestion_part_id=digestion_part_id,
        )

    @abstractmethod
    def _digestion_topic(self, **kwargs) -> models.DigestionTopicDataResponse:
        pass

    def digestion_topic(
        self, digestion_topic_id: UUID, digestion_id: Optional[UUID] = None
    ):
        return self._digestion_topic(
            digestion_topic_id=digestion_topic_id,
        )

    @abstractmethod
    def _group(self, **kwargs) -> models.GroupDataResponse:
        pass

    def group(self, group_id: UUID):
        return self._group(
            group_id=group_id,
        )

    @abstractmethod
    def _hook(self, **kwargs) -> models.HookDataResponse:
        pass

    def hook(self, hook_id: UUID, workflow_id: Optional[UUID] = None):
        return self._hook(
            workflow_id=workflow_id,
            hook_id=hook_id,
        )

    @abstractmethod
    def _ingestion(self, **kwargs) -> models.IngestionDataResponse:
        pass

    def ingestion(self, ingestion_id: UUID):
        return self._ingestion(
            ingestion_id=ingestion_id,
        )

    @abstractmethod
    def _ingestion_part(self, **kwargs) -> models.IngestionPartDataResponse:
        pass

    def ingestion_part(
        self, ingestion_part_id: UUID, ingestion_id: Optional[UUID] = None
    ):
        return self._ingestion_part(
            ingestion_id=ingestion_id,
            ingestion_part_id=ingestion_part_id,
        )

    @abstractmethod
    def _label(self, **kwargs) -> models.LabelDataResponse:
        pass

    def label(self, label_id: UUID):
        return self._label(
            label_id=label_id,
        )

    @abstractmethod
    def _log(self, **kwargs) -> models.LogDataResponse:
        pass

    def log(self, log_id: UUID):
        return self._log(
            log_id=log_id,
        )

    @abstractmethod
    def _log_object(self, **kwargs) -> models.ObjectDataResponse:
        pass

    def log_object(
        self,
        object_key: str,
        log_id: UUID,
        redirect: Optional[bool] = False,
        offset: Optional[int] = None,
        length: Optional[int] = None,
    ) -> dict | bytes:
        return self._log_object(
            log_id=log_id,
            object_key=object_key,
            redirect=redirect,
            offset=offset,
            length=length,
        )

    @abstractmethod
    def _log_object_part(self, **kwargs) -> models.ObjectPartDataResponse:
        pass

    def log_object_part(self, object_key: str, part_number: int, log_id: UUID):
        return self._log_object_part(
            object_key=object_key,
            part_number=part_number,
            log_id=log_id,
        )

    @abstractmethod
    def _object(self, **kwargs) -> models.ObjectDataResponse:
        pass

    def object(
        self,
        object_key: str,
        object_store_id: UUID,
        redirect: Optional[bool] = False,
        offset: Optional[int] = None,
        length: Optional[int] = None,
    ) -> dict | bytes:
        return self._object(
            object_store_id=object_store_id,
            object_key=object_key,
            redirect=redirect,
            offset=offset,
            length=length,
        )

    @abstractmethod
    def _object_part(self, **kwargs) -> models.ObjectPartDataResponse:
        pass

    def object_part(self, object_key: str, part_number: int, object_store_id: UUID):
        return self._object_part(
            object_key=object_key,
            part_number=part_number,
            object_store_id=object_store_id,
        )

    @abstractmethod
    def _object_store(self, **kwargs) -> models.ObjectStoreDataResponse:
        pass

    def object_store(self, object_store_id: UUID):
        return self._object_store(
            object_store_id=object_store_id,
        )

    @abstractmethod
    def _query(self, **kwargs) -> models.QueryDataResponse:
        pass

    def query(self, query_id: UUID, log_id: Optional[UUID] = None):
        return self._query(
            log_id=log_id,
            query_id=query_id,
        )

    @abstractmethod
    def _record(self, **kwargs) -> models.RecordDataResponse:
        pass

    def record(self, timestamp: float, topic_id: UUID):
        return self._record(
            timestamp=timestamp,
            topic_id=topic_id,
        )

    @abstractmethod
    def _tag(self, **kwargs) -> models.TagDataResponse:
        pass

    def tag(self, tag_id: UUID, log_id: Optional[UUID] = None):
        return self._tag(
            log_id=log_id,
            tag_id=tag_id,
        )

    @abstractmethod
    def _topic(self, **kwargs) -> models.TopicDataResponse:
        pass

    def topic(self, topic_id: UUID):
        return self._topic(
            topic_id=topic_id,
        )

    @abstractmethod
    def _workflow(self, **kwargs) -> models.WorkflowDataResponse:
        pass

    def workflow(self, workflow_id: UUID):
        return self._workflow(
            workflow_id=workflow_id,
        )
