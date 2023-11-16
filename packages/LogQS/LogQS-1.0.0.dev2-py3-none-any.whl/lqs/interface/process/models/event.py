from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from lqs.interface.process.models.__common__ import (
    CommonModel,
    PaginationModel,
    ProcessState,
    ProcessType,
    optional_field,
)


class Event(CommonModel):
    process_state: ProcessState
    process_type: ProcessType
    resource_id: UUID
    datastore_id: Optional[UUID]
    datastore_endpoint: Optional[str]


class EventDataResponse(BaseModel):
    data: Event


class EventListResponse(PaginationModel):
    data: List[Event]


class EventCreateRequest(BaseModel):
    process_state: ProcessState
    process_type: ProcessType
    resource_id: UUID
    datastore_id: Optional[UUID] = None
    datastore_endpoint: Optional[str] = None


class EventUpdateRequest(BaseModel):
    process_state: ProcessState = optional_field
    process_type: ProcessType = optional_field
    resource_id: UUID = optional_field
    datastore_id: Optional[UUID] = optional_field
    datastore_endpoint: Optional[str] = optional_field
