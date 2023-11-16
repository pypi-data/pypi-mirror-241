from abc import abstractmethod
from typing import Optional
from uuid import UUID

from lqs.interface.base.update import UpdateInterface as BaseUpdateInterface
import lqs.interface.core.models as models


class UpdateInterface(BaseUpdateInterface):
    @abstractmethod
    def _digestion(self, **kwargs) -> models.DigestionDataResponse:
        pass

    def digestion(self, digestion_id: UUID, data: dict):
        return self._digestion(
            digestion_id=digestion_id,
            data=self._process_data(data),
        )

    def _digestion_by_model(
        self, digestion_id: UUID, data: models.DigestionUpdateRequest
    ):
        return self._digestion(
            digestion_id=digestion_id,
            data=data.model_dump(exclude_unset=True),
        )

    @abstractmethod
    def _digestion_part(self, **kwargs) -> models.DigestionPartDataResponse:
        pass

    def digestion_part(
        self, digestion_part_id: UUID, data: dict, digestion_id: Optional[UUID] = None
    ):
        return self._digestion_part(
            digestion_id=digestion_id,
            digestion_part_id=digestion_part_id,
            data=self._process_data(data),
        )

    def _digestion_part_by_model(
        self,
        digestion_part_id: UUID,
        data: models.DigestionPartUpdateRequest,
        digestion_id: Optional[UUID] = None,
    ):
        return self._digestion_part(
            digestion_id=digestion_id,
            digestion_part_id=digestion_part_id,
            data=data.model_dump(exclude_unset=True),
        )

    @abstractmethod
    def _digestion_topic(self, **kwargs) -> models.DigestionTopicDataResponse:
        pass

    def digestion_topic(
        self,
        digestion_topic_id: UUID,
        data: dict,
        digestion_id: Optional[UUID] = None,
    ):
        return self._digestion_topic(
            digestion_id=digestion_id,
            digestion_topic_id=digestion_topic_id,
            data=self._process_data(data),
        )

    def _digestion_topic_by_model(
        self,
        digestion_topic_id: UUID,
        data: models.DigestionTopicUpdateRequest,
        digestion_id: Optional[UUID] = None,
    ):
        return self._digestion_topic(
            digestion_id=digestion_id,
            digestion_topic_id=digestion_topic_id,
            data=data.model_dump(exclude_unset=True),
        )

    @abstractmethod
    def _group(self, **kwargs) -> models.GroupDataResponse:
        pass

    def group(self, group_id: UUID, data: dict):
        return self._group(
            group_id=group_id,
            data=self._process_data(data),
        )

    def _group_by_model(self, group_id: UUID, data: models.GroupUpdateRequest):
        return self._group(
            group_id=group_id,
            data=data.model_dump(exclude_unset=True),
        )

    @abstractmethod
    def _hook(self, **kwargs) -> models.HookDataResponse:
        pass

    def hook(self, hook_id: UUID, data: dict, workflow_id: Optional[UUID] = None):
        return self._hook(
            workflow_id=workflow_id,
            hook_id=hook_id,
            data=self._process_data(data),
        )

    def _hook_by_model(
        self,
        hook_id: UUID,
        data: models.HookUpdateRequest,
        workflow_id: Optional[UUID] = None,
    ):
        return self._hook(
            workflow_id=workflow_id,
            hook_id=hook_id,
            data=data.model_dump(exclude_unset=True),
        )

    @abstractmethod
    def _ingestion(self, **kwargs) -> models.IngestionDataResponse:
        pass

    def ingestion(self, ingestion_id: UUID, data: dict):
        return self._ingestion(
            ingestion_id=ingestion_id,
            data=self._process_data(data),
        )

    def _ingestion_by_model(
        self, ingestion_id: UUID, data: models.IngestionUpdateRequest
    ):
        return self._ingestion(
            ingestion_id=ingestion_id,
            data=data.model_dump(exclude_unset=True),
        )

    @abstractmethod
    def _ingestion_part(self, **kwargs) -> models.IngestionPartDataResponse:
        pass

    def ingestion_part(
        self,
        ingestion_part_id: UUID,
        data: dict,
        ingestion_id: Optional[UUID] = None,
    ):
        return self._ingestion_part(
            ingestion_id=ingestion_id,
            ingestion_part_id=ingestion_part_id,
            data=self._process_data(data),
        )

    def _ingestion_part_by_model(
        self,
        ingestion_part_id: UUID,
        data: models.IngestionPartUpdateRequest,
        ingestion_id: Optional[UUID] = None,
    ):
        return self._ingestion_part(
            ingestion_id=ingestion_id,
            ingestion_part_id=ingestion_part_id,
            data=data.model_dump(exclude_unset=True),
        )

    @abstractmethod
    def _label(self, **kwargs) -> models.LabelDataResponse:
        pass

    def label(self, label_id: UUID, data: dict):
        return self._label(
            label_id=label_id,
            data=self._process_data(data),
        )

    def _label_by_model(self, label_id: UUID, data: models.LabelUpdateRequest):
        return self._label(
            label_id=label_id,
            data=data.model_dump(exclude_unset=True),
        )

    @abstractmethod
    def _log(self, **kwargs) -> models.LogDataResponse:
        pass

    def log(self, log_id: UUID, data: dict):
        return self._log(
            log_id=log_id,
            data=self._process_data(data),
        )

    def _log_by_model(self, log_id: UUID, data: models.LogUpdateRequest):
        return self._log(
            log_id=log_id,
            data=data.model_dump(exclude_unset=True),
        )

    @abstractmethod
    def _log_object(self, **kwargs) -> models.ObjectDataResponse:
        pass

    def log_object(self, log_id: UUID, object_key: str, data: dict):
        return self._log_object(
            log_id=log_id,
            object_key=object_key,
            data=self._process_data(data),
        )

    def _log_object_by_model(
        self, log_id: UUID, object_key: str, data: models.ObjectUpdateRequest
    ):
        return self._log_object(
            log_id=log_id,
            object_key=object_key,
            data=data.model_dump(exclude_unset=True),
        )

    @abstractmethod
    def _object(self, **kwargs) -> models.ObjectDataResponse:
        pass

    def object(self, object_store_id: UUID, object_key: str, data: dict):
        return self._object(
            object_store_id=object_store_id,
            object_key=object_key,
            data=self._process_data(data),
        )

    def _object_by_model(
        self, object_store_id: UUID, object_key: str, data: models.ObjectUpdateRequest
    ):
        return self._object(
            object_store_id=object_store_id,
            object_key=object_key,
            data=data.model_dump(exclude_unset=True),
        )

    @abstractmethod
    def _object_store(self, **kwargs) -> models.ObjectStoreDataResponse:
        pass

    def object_store(self, object_store_id: UUID, data: dict):
        return self._object_store(
            object_store_id=object_store_id,
            data=self._process_data(data),
        )

    def _object_store_by_model(
        self, object_store_id: UUID, data: models.ObjectStoreUpdateRequest
    ):
        return self._object_store(
            object_store_id=object_store_id,
            data=data.model_dump(exclude_unset=True),
        )

    @abstractmethod
    def _query(self, **kwargs) -> models.QueryDataResponse:
        pass

    def query(self, query_id: UUID, data: dict, log_id: Optional[UUID] = None):
        return self._query(
            log_id=log_id,
            query_id=query_id,
            data=self._process_data(data),
        )

    def _query_by_model(
        self,
        query_id: UUID,
        data: models.QueryUpdateRequest,
        log_id: Optional[UUID] = None,
    ):
        return self._query(
            log_id=log_id,
            query_id=query_id,
            data=data.model_dump(exclude_unset=True),
        )

    @abstractmethod
    def _record(self, **kwargs) -> models.RecordDataResponse:
        pass

    def record(self, timestamp: float, topic_id: UUID, data: dict):
        return self._record(
            timestamp=timestamp,
            topic_id=topic_id,
            data=self._process_data(data),
        )

    def _record_by_model(
        self, timestamp: float, topic_id: UUID, data: models.RecordUpdateRequest
    ):
        return self._record(
            timestamp=timestamp,
            topic_id=topic_id,
            data=data.model_dump(exclude_unset=True),
        )

    @abstractmethod
    def _tag(self, **kwargs) -> models.TagDataResponse:
        pass

    def tag(self, tag_id: UUID, data: dict, log_id: Optional[UUID] = None):
        return self._tag(
            log_id=log_id,
            tag_id=tag_id,
            data=self._process_data(data),
        )

    def _tag_by_model(
        self, tag_id: UUID, data: models.TagUpdateRequest, log_id: Optional[UUID] = None
    ):
        return self._tag(
            log_id=log_id,
            tag_id=tag_id,
            data=data.model_dump(exclude_unset=True),
        )

    @abstractmethod
    def _topic(self, **kwargs) -> models.TopicDataResponse:
        pass

    def topic(self, topic_id: UUID, data: dict):
        return self._topic(
            topic_id=topic_id,
            data=self._process_data(data),
        )

    def _topic_by_model(self, topic_id: UUID, data: models.TopicUpdateRequest):
        return self._topic(
            topic_id=topic_id,
            data=data.model_dump(exclude_unset=True),
        )

    @abstractmethod
    def _workflow(self, **kwargs) -> models.WorkflowDataResponse:
        pass

    def workflow(self, workflow_id: UUID, data: dict):
        return self._workflow(
            workflow_id=workflow_id,
            data=self._process_data(data),
        )

    def _workflow_by_model(self, workflow_id: UUID, data: models.WorkflowUpdateRequest):
        return self._workflow(
            workflow_id=workflow_id,
            data=data.model_dump(exclude_unset=True),
        )
