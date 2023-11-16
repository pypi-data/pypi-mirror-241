from typing import Optional, Union
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

optional_field = Field(default=None, json_schema_extra=lambda x: x.pop("default"))


class EmptyModel(BaseModel):
    pass


class ResourceModel(BaseModel):
    created_at: datetime
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]
    created_by: Optional[UUID]
    updated_by: Optional[UUID]
    deleted_by: Optional[UUID]

    model_config = ConfigDict(from_attributes=True)


class CommonModel(ResourceModel):
    id: UUID


class PaginationModel(BaseModel):
    offset: int
    limit: int
    order: str
    sort: str
    count: int


class PatchOperation(BaseModel):
    op: str
    path: str
    value: Optional[Union[str, int, float, bool, dict, list, None]]


class JSONFilter(BaseModel):
    var: str
    op: str
    val: Union[str, int, float, bool, list, None]
