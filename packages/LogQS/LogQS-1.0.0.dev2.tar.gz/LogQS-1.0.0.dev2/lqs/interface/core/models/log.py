from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from lqs.interface.core.models.__common__ import (
    CommonModel,
    PaginationModel,
    optional_field,
)


class Log(CommonModel):
    group_id: UUID
    name: str

    start_time: Optional[int]
    end_time: Optional[int]
    record_size: int
    record_count: int
    object_size: int
    object_count: int

    note: Optional[str]
    context: Optional[dict]
    locked: bool
    time_adjustment: Optional[int]
    default_workflow_id: Optional[UUID]


class LogDataResponse(BaseModel):
    data: Log


class LogListResponse(PaginationModel):
    data: List[Log]


class LogCreateRequest(BaseModel):
    group_id: UUID
    name: str
    note: Optional[str] = None
    context: Optional[dict] = None
    time_adjustment: Optional[int] = None
    default_workflow_id: Optional[UUID] = None


class LogUpdateRequest(BaseModel):
    group_id: UUID = optional_field
    name: str = optional_field

    note: Optional[str] = optional_field
    context: Optional[dict] = optional_field
    locked: bool = optional_field
    time_adjustment: Optional[int] = optional_field
    default_workflow_id: Optional[UUID] = optional_field
