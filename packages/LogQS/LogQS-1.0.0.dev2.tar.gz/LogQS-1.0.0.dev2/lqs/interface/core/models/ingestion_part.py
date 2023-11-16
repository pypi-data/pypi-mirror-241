from typing import List, Optional, Tuple
from uuid import UUID

from pydantic import BaseModel

from lqs.interface.core.models.__common__ import (
    CommonModel,
    PaginationModel,
    ProcessState,
    optional_field,
)


class IngestionPartIndexEntry(BaseModel):
    topic_id: str
    data_offset: int
    data_length: int
    chunk_compression: Optional[str]
    chunk_offset: Optional[int]
    chunk_length: Optional[int]
    timestamp: int


# TODO: in Python 3.11, we can use Tuple[*get_type_hints(IngestionPartIndex).values()]
IngestionPartIndexTuple = Tuple[
    str, int, int, Optional[str], Optional[int], Optional[int], int
]


class IngestionPartIndex(BaseModel):
    ingestion_part_id: UUID
    index: Optional[List[IngestionPartIndexTuple]]


class IngestionPartIndexCreateRequest(BaseModel):
    ingestion_part_id: UUID
    index: Optional[List[IngestionPartIndexTuple]] = None


class IngestionPartIndexUpdateRequest(BaseModel):
    index: Optional[List[IngestionPartIndexTuple]] = optional_field


class IngestionPartIndexDataResponse(BaseModel):
    data: IngestionPartIndex


class IngestionPartIndexListResponse(PaginationModel):
    data: List[IngestionPartIndex]


# Ingestion Part


class IngestionPart(CommonModel):
    sequence: int
    ingestion_id: UUID
    source: Optional[str]

    workflow_id: Optional[UUID]
    workflow_context: Optional[dict]
    state: ProcessState
    error: Optional[dict]

    index: Optional[List[IngestionPartIndexTuple]]


class IngestionPartCreateRequest(BaseModel):
    sequence: int
    source: Optional[str] = None
    workflow_id: Optional[UUID] = None
    workflow_context: Optional[dict] = None
    state: ProcessState = ProcessState.ready
    index: Optional[List[IngestionPartIndexTuple]] = None


class IngestionPartUpdateRequest(BaseModel):
    source: Optional[str] = optional_field
    workflow_id: Optional[UUID] = optional_field
    workflow_context: Optional[dict] = optional_field
    state: ProcessState = optional_field
    error: Optional[dict] = optional_field
    index: Optional[List[IngestionPartIndexTuple]] = optional_field


class IngestionPartListResponse(PaginationModel):
    data: List[IngestionPart]


class IngestionPartDataResponse(BaseModel):
    data: IngestionPart
