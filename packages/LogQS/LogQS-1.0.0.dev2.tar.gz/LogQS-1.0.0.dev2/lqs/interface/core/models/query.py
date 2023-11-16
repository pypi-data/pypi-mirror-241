from typing import List, Optional, Dict, Any
from uuid import UUID

from pydantic import BaseModel

from lqs.interface.core.models.__common__ import (
    CommonModel,
    PaginationModel,
    ProcessState,
    optional_field,
)


class Query(CommonModel):
    log_id: UUID
    name: Optional[str]

    statement: Optional[str]
    parameters: Optional[Dict[str, Any]]
    columns: Optional[List[str]]
    rows: Optional[List[List[Any]]]

    workflow_id: Optional[UUID]
    workflow_context: Optional[dict]
    state: ProcessState
    error: Optional[dict]

    note: Optional[str]
    context: Optional[dict]


class QueryDataResponse(BaseModel):
    data: Query


class QueryListResponse(PaginationModel):
    data: List[Query]


class QueryCreateRequest(BaseModel):
    name: Optional[str] = None
    note: Optional[str] = None
    statement: Optional[str] = None
    parameters: Optional[Dict[str, Any]] = None

    workflow_id: Optional[UUID] = None
    workflow_context: Optional[dict] = None
    state: ProcessState = ProcessState.ready
    context: Optional[dict] = None


class QueryUpdateRequest(BaseModel):
    name: Optional[str] = optional_field
    note: Optional[str] = optional_field
    statement: Optional[str] = optional_field
    parameters: Optional[Dict[str, Any]] = optional_field

    workflow_id: Optional[UUID] = optional_field
    workflow_context: Optional[dict] = optional_field
    state: ProcessState = optional_field
    error: Optional[dict] = optional_field
    context: Optional[dict] = optional_field
