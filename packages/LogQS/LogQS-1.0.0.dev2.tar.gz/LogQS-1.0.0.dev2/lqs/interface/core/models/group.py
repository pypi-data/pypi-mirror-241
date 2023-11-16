from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from lqs.interface.core.models.__common__ import (
    CommonModel,
    PaginationModel,
    optional_field,
)


class Group(CommonModel):
    name: str
    default_workflow_id: Optional[UUID]


class GroupDataResponse(BaseModel):
    data: Group


class GroupListResponse(PaginationModel):
    data: List[Group]


class GroupCreateRequest(BaseModel):
    name: str
    default_workflow_id: Optional[UUID] = None


class GroupUpdateRequest(BaseModel):
    name: str = optional_field
    default_workflow_id: Optional[UUID] = optional_field
