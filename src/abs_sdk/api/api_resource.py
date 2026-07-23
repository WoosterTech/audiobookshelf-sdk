from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

type QueryValue = str | int | float | bool | None

if TYPE_CHECKING:
    from collections.abc import Mapping

    from abs_sdk.core import QueryParamTypes, URLTypes


class SupportsRequestJson(Protocol):
    def request_json(
        self,
        method: str,
        path: URLTypes,
        *,
        params: QueryParamTypes | None = None,
        json_body: Mapping[str, object] | None = None,
    ) -> object: ...


class APIResource:
    """Base class for namespaced API resources."""

    def __init__(self, client: SupportsRequestJson) -> None:
        self._client: SupportsRequestJson = client
