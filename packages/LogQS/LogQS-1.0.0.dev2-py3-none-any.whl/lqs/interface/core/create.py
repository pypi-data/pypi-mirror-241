from abc import abstractmethod
from typing import List, Optional
from uuid import UUID

from lqs.interface.base.create import CreateInterface as BaseCreateInterface
import lqs.interface.core.models as models


class CreateInterface(BaseCreateInterface):
    @abstractmethod
    def _digestion(self, **kwargs) -> models.DigestionDataResponse:
        pass

    def digestion(
        self,
        log_id: UUID,
        name: Optional[str] = None,
        workflow_id: Optional[UUID] = None,
        workflow_context: Optional[dict] = None,
        note: Optional[str] = None,
        context: Optional[dict] = None,
        state: str = "ready",
    ):
        return self._digestion(
            log_id=log_id,
            name=name,
            workflow_id=workflow_id,
            workflow_context=workflow_context,
            note=note,
            context=context,
            state=state,
        )

    def _digestion_by_model(self, data: models.DigestionCreateRequest):
        return self.digestion(**data.model_dump())

    @abstractmethod
    def _digestion_part(self, **kwargs) -> models.DigestionPartDataResponse:
        pass

    def digestion_part(
        self,
        digestion_id: UUID,
        sequence: int,
        workflow_id: Optional[UUID] = None,
        workflow_context: Optional[dict] = None,
        state: str = "queued",
        index: Optional[List[models.DigestionPartIndex]] = None,
    ):
        return self._digestion_part(
            digestion_id=digestion_id,
            sequence=sequence,
            workflow_id=workflow_id,
            workflow_context=workflow_context,
            state=state,
            index=index,
        )

    def _digestion_part_by_model(
        self, digestion_id: UUID, data: models.DigestionPartCreateRequest
    ):
        return self.digestion_part(digestion_id=digestion_id, **data.model_dump())

    @abstractmethod
    def _digestion_topic(self, **kwargs) -> models.DigestionTopicDataResponse:
        pass

    def digestion_topic(
        self,
        digestion_id: UUID,
        topic_id: UUID,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        frequency: Optional[float] = None,
        data_filter: Optional[dict] = None,
        context_filter: Optional[dict] = None,
    ):
        return self._digestion_topic(
            digestion_id=digestion_id,
            topic_id=topic_id,
            start_time=start_time,
            end_time=end_time,
            frequency=frequency,
            data_filter=data_filter,
            context_filter=context_filter,
        )

    def _digestion_topic_by_model(
        self, digestion_id: UUID, data: models.DigestionTopicCreateRequest
    ):
        return self.digestion_topic(digestion_id=digestion_id, **data.model_dump())

    @abstractmethod
    def _group(self, **kwargs) -> models.GroupDataResponse:
        pass

    def group(
        self,
        name: str,
        default_workflow_id: Optional[UUID] = None,
    ):
        return self._group(
            name=name,
            default_workflow_id=default_workflow_id,
        )

    def _group_by_model(self, data: models.GroupCreateRequest):
        return self.group(**data.model_dump())

    @abstractmethod
    def _hook(self, **kwargs) -> models.HookDataResponse:
        pass

    def hook(
        self,
        workflow_id: UUID,
        trigger_process: str,
        trigger_state: str,
        name: Optional[str] = None,
        note: Optional[str] = None,
        managed: Optional[bool] = False,
        disabled: Optional[bool] = False,
        uri: Optional[str] = None,
        secret: Optional[str] = None,
    ):
        return self._hook(
            workflow_id=workflow_id,
            trigger_process=trigger_process,
            trigger_state=trigger_state,
            name=name,
            note=note,
            managed=managed,
            disabled=disabled,
            uri=uri,
            secret=secret,
        )

    def _hook_by_model(self, workflow_id: UUID, data: models.HookCreateRequest):
        return self.hook(workflow_id=workflow_id, **data.model_dump())

    @abstractmethod
    def _ingestion(self, **kwargs) -> models.IngestionDataResponse:
        pass

    def ingestion(
        self,
        log_id: UUID,
        name: Optional[str] = None,
        object_store_id: Optional[UUID] = None,
        object_key: Optional[str] = None,
        workflow_id: Optional[UUID] = None,
        workflow_context: Optional[dict] = None,
        state: str = "ready",
        note: Optional[str] = None,
        context: Optional[dict] = None,
    ):
        return self._ingestion(
            log_id=log_id,
            name=name,
            object_store_id=object_store_id,
            object_key=object_key,
            workflow_id=workflow_id,
            workflow_context=workflow_context,
            state=state,
            note=note,
            context=context,
        )

    def _ingestion_by_model(self, data: models.IngestionCreateRequest):
        return self.ingestion(**data.model_dump())

    @abstractmethod
    def _ingestion_part(self, **kwargs) -> models.IngestionPartDataResponse:
        pass

    def ingestion_part(
        self,
        ingestion_id: UUID,
        sequence: int,
        source: Optional[str] = None,
        workflow_id: Optional[UUID] = None,
        workflow_context: Optional[dict] = None,
        state: str = "queued",
        index: Optional[List[models.IngestionPartIndex]] = None,
    ):
        return self._ingestion_part(
            ingestion_id=ingestion_id,
            sequence=sequence,
            source=source,
            workflow_id=workflow_id,
            workflow_context=workflow_context,
            state=state,
            index=index,
        )

    def _ingestion_part_by_model(
        self, ingestion_id: UUID, data: models.IngestionPartCreateRequest
    ):
        return self.ingestion_part(ingestion_id=ingestion_id, **data.model_dump())

    @abstractmethod
    def _label(self, **kwargs) -> models.LabelDataResponse:
        pass

    def label(self, value: str, note: Optional[str] = None):
        return self._label(
            value=value,
            note=note,
        )

    def _label_by_model(self, data: models.LabelCreateRequest):
        return self.label(**data.model_dump())

    @abstractmethod
    def _log(self, **kwargs) -> models.LogDataResponse:
        pass

    def log(
        self,
        group_id: UUID,
        name: str,
        note: Optional[str] = None,
        context: Optional[dict] = None,
        time_adjustment: Optional[int] = None,
        default_workflow_id: Optional[UUID] = None,
    ):
        return self._log(
            group_id=group_id,
            name=name,
            note=note,
            context=context,
            time_adjustment=time_adjustment,
            default_workflow_id=default_workflow_id,
        )

    def _log_by_model(self, data: models.LogCreateRequest):
        return self.log(**data.model_dump())

    @abstractmethod
    def _log_object(self, **kwargs) -> models.ObjectDataResponse:
        pass

    def log_object(
        self,
        key: str,
        log_id: UUID,
        content_type: Optional[str] = None,
    ):
        return self._log_object(
            key=key,
            log_id=log_id,
            content_type=content_type,
        )

    def _log_object_by_model(self, log_id: UUID, data: models.ObjectCreateRequest):
        return self.log_object(log_id=log_id, **data.model_dump())

    @abstractmethod
    def _log_object_part(self, **kwargs) -> models.ObjectPartDataResponse:
        pass

    def log_object_part(
        self,
        object_key: str,
        size: int,
        log_id: UUID,
        part_number: Optional[int] = None,
    ):
        return self._log_object_part(
            object_key=object_key,
            log_id=log_id,
            part_number=part_number,
            size=size,
        )

    def _log_object_part_by_model(
        self, object_key: str, log_id: UUID, data: models.ObjectPartCreateRequest
    ):
        return self.log_object_part(
            object_key=object_key, log_id=log_id, **data.model_dump()
        )

    @abstractmethod
    def _object(self, **kwargs) -> models.ObjectDataResponse:
        pass

    def object(
        self,
        key: str,
        object_store_id: UUID,
        content_type: Optional[str] = None,
    ):
        return self._object(
            key=key,
            object_store_id=object_store_id,
            content_type=content_type,
        )

    def _object_by_model(self, object_store_id: UUID, data: models.ObjectCreateRequest):
        return self.object(object_store_id=object_store_id, **data.model_dump())

    @abstractmethod
    def _object_part(self, **kwargs) -> models.ObjectPartDataResponse:
        pass

    def object_part(
        self,
        object_key: str,
        size: int,
        object_store_id: UUID,
        part_number: Optional[int] = None,
    ):
        return self._object_part(
            object_key=object_key,
            object_store_id=object_store_id,
            part_number=part_number,
            size=size,
        )

    def _object_part_by_model(
        self,
        object_key: str,
        object_store_id: UUID,
        data: models.ObjectPartCreateRequest,
    ):
        return self.object_part(
            object_key=object_key, object_store_id=object_store_id, **data.model_dump()
        )

    @abstractmethod
    def _object_store(self, **kwargs) -> models.ObjectStoreDataResponse:
        pass

    def object_store(
        self,
        bucket_name: str,
        access_key_id: Optional[str] = None,
        secret_access_key: Optional[str] = None,
        region_name: Optional[str] = None,
        endpoint_url: Optional[str] = None,
        note: Optional[str] = None,
        disabled: Optional[bool] = False,
    ):
        return self._object_store(
            bucket_name=bucket_name,
            access_key_id=access_key_id,
            secret_access_key=secret_access_key,
            region_name=region_name,
            endpoint_url=endpoint_url,
            note=note,
            disabled=disabled,
        )

    def _object_store_by_model(self, data: models.ObjectStoreCreateRequest):
        return self.object_store(**data.model_dump())

    @abstractmethod
    def _query(self, **kwargs) -> models.QueryDataResponse:
        pass

    def query(
        self,
        log_id: UUID,
        name: Optional[str] = None,
        note: Optional[str] = None,
        statement: Optional[str] = None,
        parameters: Optional[dict] = None,
        workflow_id: Optional[UUID] = None,
        workflow_context: Optional[dict] = None,
        state: str = "queued",
        error: Optional[dict] = None,
        context: Optional[dict] = None,
    ):
        return self._query(
            log_id=log_id,
            name=name,
            note=note,
            statement=statement,
            parameters=parameters,
            workflow_id=workflow_id,
            workflow_context=workflow_context,
            state=state,
            error=error,
            context=context,
        )

    def _query_by_model(self, log_id: UUID, data: models.QueryCreateRequest):
        return self.query(log_id=log_id, **data.model_dump())

    @abstractmethod
    def _record(self, **kwargs) -> models.RecordDataResponse:
        pass

    def record(
        self,
        timestamp: int,
        topic_id: UUID,
        data_offset: Optional[int] = None,
        data_length: Optional[int] = None,
        chunk_compression: Optional[str] = None,
        chunk_offset: Optional[int] = None,
        chunk_length: Optional[int] = None,
        source: Optional[str] = None,
        workflow_id: Optional[UUID] = None,
        workflow_context: Optional[dict] = None,
        state: str = "completed",
        note: Optional[str] = None,
        data: Optional[dict] = None,
        context: Optional[dict] = None,
    ):
        return self._record(
            timestamp=timestamp,
            topic_id=topic_id,
            data_offset=data_offset,
            data_length=data_length,
            chunk_compression=chunk_compression,
            chunk_offset=chunk_offset,
            chunk_length=chunk_length,
            workflow_id=workflow_id,
            workflow_context=workflow_context,
            state=state,
            note=note,
            source=source,
            data=data,
            context=context,
        )

    def _record_by_model(self, topic_id: UUID, data: models.RecordCreateRequest):
        return self.record(topic_id=topic_id, **data.model_dump())

    @abstractmethod
    def _tag(self, **kwargs) -> models.TagDataResponse:
        pass

    def tag(
        self,
        label_id: UUID,
        log_id: UUID,
        topic_id: Optional[UUID] = None,
        note: Optional[str] = None,
        context: Optional[dict] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
    ):
        return self._tag(
            label_id=label_id,
            log_id=log_id,
            topic_id=topic_id,
            note=note,
            context=context,
            start_time=start_time,
            end_time=end_time,
        )

    def _tag_by_model(self, log_id: UUID, data: models.TagCreateRequest):
        return self.tag(log_id=log_id, **data.model_dump())

    @abstractmethod
    def _topic(self, **kwargs) -> models.TopicDataResponse:
        pass

    def topic(
        self,
        log_id: UUID,
        name: str,
        associated_topic_id: Optional[UUID] = None,
        latched: Optional[bool] = False,
        strict: Optional[bool] = False,
        context: Optional[dict] = None,
        type_name: Optional[str] = None,
        type_encoding: Optional[str] = None,
        type_data: Optional[str] = None,
        type_schema: Optional[dict] = None,
    ):
        return self._topic(
            name=name,
            log_id=log_id,
            associated_topic_id=associated_topic_id,
            latched=latched,
            strict=strict,
            context=context,
            type_name=type_name,
            type_encoding=type_encoding,
            type_data=type_data,
            type_schema=type_schema,
        )

    def _topic_by_model(self, data: models.TopicCreateRequest):
        return self.topic(**data.model_dump())

    @abstractmethod
    def _workflow(self, **kwargs) -> models.WorkflowDataResponse:
        pass

    def workflow(
        self,
        name: str,
        note: Optional[str] = None,
        default: Optional[bool] = False,
        disabled: Optional[bool] = False,
        managed: Optional[bool] = False,
        context_schema: Optional[dict] = None,
    ):
        return self._workflow(
            name=name,
            note=note,
            default=default,
            disabled=disabled,
            managed=managed,
            context_schema=context_schema,
        )

    def _workflow_by_model(self, data: models.WorkflowCreateRequest):
        return self.workflow(**data.model_dump())
