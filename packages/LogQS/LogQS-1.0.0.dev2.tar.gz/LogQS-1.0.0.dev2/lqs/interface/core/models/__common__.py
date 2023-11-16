from enum import Enum

from lqs.interface.base.models.__common__ import (  # noqa: F401
    ResourceModel,
    CommonModel,
    PaginationModel,
    PatchOperation,
    JSONFilter,
    optional_field,
)


class TimeSeriesModel(ResourceModel):
    timestamp: int


class ProcessState(str, Enum):
    ready = "ready"
    queued = "queued"
    processing = "processing"
    finalizing = "finalizing"
    completed = "completed"
    errored = "errored"
    cancelled = "cancelled"
    archived = "archived"


class ProcessType(str, Enum):
    ingestion = "ingestion"
    ingestion_part = "ingestion_part"
    digestion = "digestion"
    digestion_part = "digestion_part"
    query = "query"
    record = "record"


class TypeEncoding(str, Enum):
    ros1 = "ros1"
    rbuf = "rbuf"
