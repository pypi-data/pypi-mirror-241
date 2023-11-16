from typing import List, Optional
from enum import Enum

from pydantic import BaseModel

from lqs.interface.base.models.__common__ import (
    CommonModel,
    PaginationModel,
    optional_field,
)


class EffectEnum(str, Enum):
    allow = "allow"
    deny = "deny"


class Statement(BaseModel):
    effect: EffectEnum
    action: List[str]
    resource: List[str]


class Policy(BaseModel):
    statement: List[Statement]


class Role(CommonModel):
    name: str
    policy: Policy
    note: Optional[str]

    disabled: bool
    default: bool
    managed: bool


class RoleDataResponse(BaseModel):
    data: Role


class RoleListResponse(PaginationModel):
    data: List[Role]


class RoleCreateRequest(BaseModel):
    name: str
    policy: dict

    note: Optional[str] = None
    disabled: bool = False
    managed: bool = False
    default: bool = False


class RoleUpdateRequest(BaseModel):
    name: str = optional_field
    policy: dict = optional_field
    note: Optional[str] = optional_field
    disabled: bool = optional_field
    default: bool = optional_field
