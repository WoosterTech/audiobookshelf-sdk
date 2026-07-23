from __future__ import annotations

from httpx import QueryParams
from yarl import URL

from abs_sdk.api.api_resource import APIResource
from abs_sdk.response.me import ItemsInProgressResponse
from abs_sdk.response.media_progress import MediaProgressResponse


class MeAPI(APIResource):
    """Endpoints under /api/me."""

    def get_library_items_in_progress(self, *, limit: int | None = None) -> ItemsInProgressResponse:
        """Get a list of library items that are in progress for the current user."""
        params: QueryParams = QueryParams()
        if limit is not None:
            params = params.add("limit", limit)
        response = self._client.request_json("GET", "/api/me/items-in-progress", params=params)
        return ItemsInProgressResponse.model_validate(response)

    def get_media_progress(
        self, library_item_id: str, *, episode_id: str | None = None
    ) -> MediaProgressResponse:
        """Get the media progress for a specific library item and optional episode."""
        path = URL("api/me/progress/") / library_item_id
        if episode_id is not None:
            path /= episode_id
        response = self._client.request_json("GET", path)
        return MediaProgressResponse.model_validate(response)
