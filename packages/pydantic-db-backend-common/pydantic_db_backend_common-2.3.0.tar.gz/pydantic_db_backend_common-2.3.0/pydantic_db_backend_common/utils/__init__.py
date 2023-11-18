from __future__ import annotations

import datetime
from contextvars import ContextVar
from typing import Any, Type
from uuid import uuid4

import iso8601
from iso8601 import ParseError


def uid() -> str:
    return str(uuid4()).replace("-", "")


_uid = uid


def utcnow() -> datetime.datetime:
    return datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)


def str_to_datetime_if_parseable(value: str) -> datetime.datetime | str:
    if len(value) < 8 or value.count("-") != 2:
        return value
    try:
        ret = iso8601.parse_date(value)
    except (ParseError, ValueError, TypeError):
        ret = value
    return ret


class Undefined:
    pass


def resolve_undefined_type_context(
    context_var: ContextVar,
    new_type: Any,
    parameter: Any | None | Type[Undefined] = Undefined,
) -> Any:
    if parameter is Undefined:
        parameter = context_var.get()
    elif parameter is None:
        parameter = new_type()
    return parameter
