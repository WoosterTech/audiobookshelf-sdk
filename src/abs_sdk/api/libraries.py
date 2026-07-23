"""Created by abs_sdk.devtools.create_module."""

from typing import TYPE_CHECKING

from attrmagic.sentinels import MISSING, Missing
from httpx import QueryParams

from abs_sdk.api.api_resource import APIResource
from abs_sdk.core import APIResponseModel
from abs_sdk.logging_config import get_logger
from abs_sdk.response.library import LibraryResponse, LibrarysItemsResponse
from abs_sdk.response.library_filter_data import LibraryFilterDataResponse  # noqa: TC001

if TYPE_CHECKING:
    from collections.abc import Iterable
    from uuid import UUID

logger = get_logger(__name__)


class LibrariesResponse(APIResponseModel):
    """A response model representing a list of libraries."""

    libraries: list[LibraryResponse]


class GetLibraryResponse(APIResponseModel):
    """A response model representing a single library."""

    filterdata: LibraryFilterDataResponse | Missing = MISSING
    issues: int
    num_user_playlists: int
    library: LibraryResponse


class LibrariesAPI(APIResource):
    """Endpoints under /api/libraries."""

    def get_all_libraries(self) -> LibrariesResponse:
        """Get a list of all libraries accessible to the user."""
        response = self._client.request_json("GET", "/api/libraries")
        return LibrariesResponse.model_validate(response)

    def get_a_library(
        self, library_id: "UUID | str", *, include: "Iterable[str] | None" = None
    ) -> LibraryResponse:
        """Get details of a specific library by its ID."""
        query_params = QueryParams()
        if include is not None:
            if "filterdata" in include:
                logger.warning(
                    "Requesting filterdata for a library. The response model may not fully support this yet."
                )
            query_params = query_params.add("include", ",".join(include))
        response = self._client.request_json(
            "GET", f"/api/libraries/{library_id}", params=query_params
        )
        return LibraryResponse.model_validate(response)

    def get_library_items(
        self,
        library_id: "UUID | str",
        *,
        limit: int | None = None,
        page: int | None = None,
        sort: str | None = None,
        desc: bool = False,
        filter: str | None = None,
        minified: bool = False,
        collapseseries: bool = False,
        include: "Iterable[str] | None" = None,
    ) -> LibrarysItemsResponse:
        """Get a list of items in a specific library by its ID."""
        query_params = QueryParams()
        if limit is not None:
            query_params = query_params.add("limit", limit)
        if page is not None:
            query_params = query_params.add("page", page)
        if sort is not None:
            query_params = query_params.add("sort", sort)
        if desc:
            query_params = query_params.add("desc", 1)
        if filter is not None:
            query_params = query_params.add("filter", filter)
        # TODO: response model should be updated to support minified response
        if minified:
            query_params = query_params.add("minified", 1)
        else:
            logger.warning(
                "Requesting non-minified library items. The response model may not fully support this yet."
            )
            query_params = query_params.add("minified", 0)
        # TODO: response model should be updated to support collapseseries response
        if collapseseries:
            logger.warning(
                "Requesting collapsed series library items. The response model may not fully support this yet."
            )
            query_params = query_params.add("collapseseries", 1)
        if include is not None:
            query_params = query_params.add("include", ",".join(include))
        response = self._client.request_json(
            "GET", f"/api/libraries/{library_id}/items", params=query_params
        )
        return LibrarysItemsResponse.model_validate(response)
