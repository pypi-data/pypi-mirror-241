from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from lqs.interface.core.models.__common__ import (
    TimeSeriesModel,
    PaginationModel,
    ProcessState,
    optional_field,
)


class Record(TimeSeriesModel):
    timestamp: int
    topic_id: UUID
    log_id: UUID
    ingestion_id: Optional[UUID]

    data_offset: Optional[int]
    data_length: Optional[int]
    chunk_compression: Optional[str]
    chunk_offset: Optional[int]
    chunk_length: Optional[int]
    source: Optional[str]

    workflow_id: Optional[UUID]
    workflow_context: Optional[dict]
    state: ProcessState
    error: Optional[dict]

    data: Optional[dict]
    context: Optional[dict]
    altered: Optional[bool]
    note: Optional[str]


class RecordDataResponse(BaseModel):
    data: Record


class RecordListResponse(PaginationModel):
    data: List[Record]


class RecordCreateRequest(BaseModel):
    timestamp: int
    workflow_id: Optional[UUID] = None
    workflow_context: Optional[dict] = None
    state: ProcessState = ProcessState.ready
    data: Optional[dict] = None
    context: Optional[dict] = None
    note: Optional[str] = None

    data_offset: Optional[int] = None
    data_length: Optional[int] = None
    chunk_compression: Optional[str] = None
    chunk_offset: Optional[int] = None
    chunk_length: Optional[int] = None
    source: Optional[str] = None


class RecordUpdateRequest(BaseModel):
    workflow_id: Optional[UUID] = optional_field
    workflow_context: Optional[dict] = optional_field
    state: ProcessState = optional_field
    error: Optional[dict] = optional_field
    data: Optional[dict] = optional_field
    context: Optional[dict] = optional_field
    altered: Optional[bool] = optional_field
    note: Optional[str] = optional_field


# Record Objects


class RecordObject(BaseModel):
    timestamp: int
    presigned_url: Optional[str] = None


class RecordObjectDataResponse(BaseModel):
    data: RecordObject


class RecordObjectListResponse(PaginationModel):
    data: List[RecordObject]
