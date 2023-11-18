from __future__ import annotations

from typing import Type, Callable, List

from pydantic import BaseModel

from pydantic_db_backend_common.pydantic import PaginationResponseModel


def pagination_convert_response_list(
    response: PaginationResponseModel,
    model: Type[BaseModel] | None = None,
    callback: Callable[[dict], BaseModel] | None = None,
) -> List[BaseModel]:
    if model is None and callback is None:
        raise ValueError("Either model or callback needs to be defined.")
    if model is not None and callback is not None:
        raise ValueError("Only one parameter can be specified. Either model or callback.")

    if model is not None:
        return [model.model_validate(response.data[uid]) for uid in response.ids]

    if callback is not None:
        return [callback(response.data[uid]) for uid in response.ids]
