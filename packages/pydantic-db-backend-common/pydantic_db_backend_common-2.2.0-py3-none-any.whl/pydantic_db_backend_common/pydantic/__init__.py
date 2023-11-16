from __future__ import annotations

import datetime
from typing import Dict, List, Any

from pydantic import BaseModel, Field, ConfigDict

from pydantic_db_backend_common.utils import utcnow, uid


class BackendModel(BaseModel):
    uid: str | None = Field(default_factory=uid)
    revision: str | None = None
    version: int | None = 1
    created_time: datetime.datetime | None = Field(default_factory=utcnow)
    updated_time: datetime.datetime | None = Field(default_factory=utcnow)



class PaginationParameterModel(BaseModel):
    skip: int | None = None
    limit: int | None = None
    sort: str | None = None
    view: str | None = None
    filter: dict | None = None


class PaginationResponseModel(BaseModel):
    data: Dict[str, dict] = {}
    skip: int | None = Field(None, nullable=True)
    limit: int | None = Field(None, nullable=True)
    max_results: int | None = None
    sort: dict | None = None
    view: str | None = None
    ids: List[str] | None = []


class FindResultModel(BaseModel):
    data: List[Any] | None = []
    max_results: int | None = None


class AggregationModel(BaseModel):
    pipeline: List[dict] = []
    use_facet: bool | None = False


class CustomAggregationModel(BaseModel):
    before_tail: List[dict] | None = None
