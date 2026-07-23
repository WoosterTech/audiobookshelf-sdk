from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

import httpx
from yarl import URL

from abs_sdk.core import QueryParamTypes, SecretToken, URLTypes

if TYPE_CHECKING:
    from collections.abc import Mapping


class AudiobookshelfClient:
    """HTTP client for the Audiobookshelf API."""

    def __init__(
        self,
        *,
        base_url: URLTypes,
        token: str,
        timeout_seconds: float = 30.0,
        verify_ssl: bool = True,
    ) -> None:
        self._base_url: URL = URL(base_url)
        self._token: SecretToken = SecretToken(token)
        self._client: httpx.Client = httpx.Client(timeout=timeout_seconds, verify=verify_ssl)
        from abs_sdk.api.libraries import LibrariesAPI
        from abs_sdk.api.me import MeAPI

        self.me: MeAPI = MeAPI(self)
        self.libraries: LibrariesAPI = LibrariesAPI(self)

    @property
    def base_url(self) -> URL:
        """Return the configured Audiobookshelf server URL."""
        return self._base_url

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def _build_url_str(self, path: URLTypes) -> str:
        """Build a full URL for a given API path."""
        return str(self._base_url / str(path).lstrip("/"))

    def _headers(self) -> httpx.Headers:
        """Return the headers for requests, including the Authorization header."""
        return httpx.Headers({"Authorization": f"Bearer {self._token.get_secret_value()}"})

    def request_json(
        self,
        method: str,
        path: URLTypes,
        *,
        params: QueryParamTypes | None = None,
        json_body: Mapping[str, object] | None = None,
    ) -> object:
        """Send a request and return decoded JSON, raising on HTTP errors."""
        response = self._client.request(
            method=method,
            url=self._build_url_str(path),
            headers=self._headers(),
            params=params,
            json=json_body,
        )
        response = response.raise_for_status()
        return cast("object", response.json())
