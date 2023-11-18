from typing import Any

from pydantic.main import BaseModel

from airfold_common.type import Schema


class Spec(BaseModel):
    name: str
    spec: Any


class AISpec(BaseModel):
    system: str
    host: str


class AIRequestParams(BaseModel):
    database: str
    table: str
    spec: str
    format: Schema
    message: str
