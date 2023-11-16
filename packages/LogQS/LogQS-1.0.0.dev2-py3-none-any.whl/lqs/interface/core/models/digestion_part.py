from typing import List, Optional, Tuple
from uuid import UUID

from pydantic import BaseModel

from lqs.interface.core.models.__common__ import (
    CommonModel,
    PaginationModel,
    ProcessState,
    optional_field,
)


class DigestionPartIndexEntry(BaseModel):
    topic_id: str
    ingestion_id: Optional[str]
    source: Optional[str]

    data_offset: int
    data_length: int

    chunk_compression: Optional[str]
    chunk_offset: Optional[int]
    chunk_length: Optional[int]
    timestamp: int


# TODO: in Python 3.11, we can use Tuple[*get_type_hints(DigestionPartIndex).values()]
DigestionPartIndexTuple = Tuple[
    str,
    Optional[str],
    Optional[str],
    int,
    int,
    Optional[str],
    Optional[int],
    Optional[int],
    int,
]


class DigestionPartIndex(BaseModel):
    digestion_part_id: UUID
    index: Optional[List[DigestionPartIndexTuple]]


class DigestionPartIndexCreateRequest(BaseModel):
    digestion_part_id: UUID
    index: Optional[List[DigestionPartIndexTuple]] = None


class DigestionPartIndexUpdateRequest(BaseModel):
    index: Optional[List[DigestionPartIndexTuple]] = optional_field


class DigestionPartIndexDataResponse(BaseModel):
    data: DigestionPartIndex


class DigestionPartIndexListResponse(PaginationModel):
    data: List[DigestionPartIndex]


# Digestion Part


class DigestionPart(CommonModel):
    sequence: int
    digestion_id: UUID

    workflow_id: Optional[UUID]
    workflow_context: Optional[dict]
    state: ProcessState
    error: Optional[dict]

    index: Optional[List[DigestionPartIndexTuple]]


class DigestionPartCreateRequest(BaseModel):
    sequence: int
    workflow_id: Optional[UUID] = None
    workflow_context: Optional[dict] = None
    state: ProcessState = ProcessState.ready
    index: Optional[List[DigestionPartIndexTuple]] = None


class DigestionPartUpdateRequest(BaseModel):
    workflow_id: Optional[UUID] = optional_field
    workflow_context: Optional[dict] = optional_field
    state: ProcessState = optional_field
    error: Optional[dict] = optional_field
    index: Optional[List[DigestionPartIndexTuple]] = optional_field


class DigestionPartDataResponse(BaseModel):
    data: DigestionPart


class DigestionPartListResponse(PaginationModel):
    data: List[DigestionPart]
