from typing import List

from pydantic import BaseModel

from lqs.interface.dsm.models.__common__ import (
    CommonModel,
    PaginationModel,
    optional_field,
)


class DataStore(CommonModel):
    name: str


class DataStoreDataResponse(BaseModel):
    data: DataStore


class DataStoreListResponse(PaginationModel):
    data: List[DataStore]


class DataStoreCreateRequest(BaseModel):
    name: str


class DataStoreUpdateRequest(BaseModel):
    name: str = optional_field
