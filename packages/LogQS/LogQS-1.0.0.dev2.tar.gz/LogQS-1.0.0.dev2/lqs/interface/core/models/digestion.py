from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from lqs.interface.core.models.__common__ import (
    CommonModel,
    PaginationModel,
    ProcessState,
    optional_field,
)


class Digestion(CommonModel):
    log_id: UUID
    name: Optional[str]
    note: Optional[str]
    context: Optional[dict]
    progress: Optional[float]

    workflow_id: Optional[UUID]
    workflow_context: Optional[dict]
    state: ProcessState
    error: Optional[dict]


class DigestionDataResponse(BaseModel):
    data: Digestion


class DigestionListResponse(PaginationModel):
    data: List[Digestion]


class DigestionCreateRequest(BaseModel):
    log_id: UUID
    name: Optional[str] = None
    workflow_id: Optional[UUID] = None
    workflow_context: Optional[dict] = None
    note: Optional[str] = None
    context: Optional[dict] = None
    state: ProcessState = ProcessState.ready


class DigestionUpdateRequest(BaseModel):
    name: Optional[str] = optional_field
    workflow_context: Optional[dict] = optional_field

    state: ProcessState = optional_field
    progress: Optional[float] = optional_field
    error: Optional[dict] = optional_field
    note: Optional[str] = optional_field
    context: Optional[dict] = optional_field
