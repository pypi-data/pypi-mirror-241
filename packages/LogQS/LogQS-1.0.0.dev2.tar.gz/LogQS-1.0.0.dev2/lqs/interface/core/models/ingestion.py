from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from lqs.interface.core.models.__common__ import (
    CommonModel,
    PaginationModel,
    ProcessState,
    optional_field,
)


class Ingestion(CommonModel):
    log_id: UUID
    object_store_id: Optional[UUID]

    object_key: Optional[str]
    name: Optional[str]
    workflow_id: Optional[UUID]
    workflow_context: Optional[dict]
    state: ProcessState
    error: Optional[dict]

    progress: Optional[float]
    note: Optional[str]
    context: Optional[dict]


class IngestionDataResponse(BaseModel):
    data: Ingestion


class IngestionListResponse(PaginationModel):
    data: List[Ingestion]


class IngestionCreateRequest(BaseModel):
    log_id: UUID
    name: Optional[str] = None
    object_store_id: Optional[UUID] = None
    object_key: Optional[str] = None
    workflow_id: Optional[UUID] = None
    workflow_context: Optional[dict] = None
    state: ProcessState = ProcessState.ready
    note: Optional[str] = None
    context: Optional[dict] = None


class IngestionUpdateRequest(BaseModel):
    name: Optional[str] = optional_field
    object_store_id: Optional[UUID] = optional_field
    object_key: Optional[str] = optional_field
    workflow_id: Optional[UUID] = optional_field
    workflow_context: Optional[dict] = optional_field

    state: ProcessState = optional_field
    progress: Optional[float] = optional_field
    error: Optional[dict] = optional_field
    note: Optional[str] = optional_field
    context: Optional[dict] = optional_field
