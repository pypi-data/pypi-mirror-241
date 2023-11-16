from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from lqs.interface.core.models.__common__ import (
    CommonModel,
    PaginationModel,
    TypeEncoding,
    optional_field,
)


class Topic(CommonModel):
    name: str
    log_id: UUID
    associated_topic_id: Optional[UUID]

    start_time: Optional[int]
    end_time: Optional[int]
    record_size: int
    record_count: int

    locked: bool
    latched: bool
    strict: bool
    context: Optional[dict]

    type_name: Optional[str]
    type_encoding: Optional[TypeEncoding]
    type_data: Optional[str]
    type_schema: Optional[dict]


class TopicDataResponse(BaseModel):
    data: Topic


class TopicListResponse(PaginationModel):
    data: List[Topic]


class TopicCreateRequest(BaseModel):
    name: str
    log_id: UUID
    associated_topic_id: Optional[UUID] = None

    latched: bool = False
    strict: bool = False
    context: Optional[dict] = None

    type_name: Optional[str] = None
    type_encoding: Optional[TypeEncoding] = None
    type_data: Optional[str] = None
    type_schema: Optional[dict] = None


class TopicUpdateRequest(BaseModel):
    name: str = optional_field
    associated_topic_id: Optional[UUID] = optional_field

    latched: bool = optional_field
    strict: bool = optional_field
    locked: bool = optional_field
    context: Optional[dict] = optional_field
