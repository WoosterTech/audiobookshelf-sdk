"""Created by abs_sdk.devtools.create_module."""

from typing import Annotated, Literal
from uuid import UUID  # noqa: TC003

from attrmagic.sentinels import MISSING, Missing
from pydantic import Field

from abs_sdk.core import APIResponseModel, MediaType, datetime_from_epoch_ms
from abs_sdk.logging_config import get_logger
from abs_sdk.response.folder import FolderResponse  # noqa: TC001
from abs_sdk.response.library_item import LibraryItemsResponseMinified  # noqa: TC001
from abs_sdk.response.library_settings import LibrarySettingsResponse  # noqa: TC001

logger = get_logger(__name__)


class LibraryResponse(APIResponseModel):
    id: UUID
    name: str
    folders: list[FolderResponse]
    display_order: Annotated[int, Field(ge=1)]
    icon: str
    media_type: MediaType
    provider: str
    settings: LibrarySettingsResponse
    created_at: int
    last_update: int

    @property
    def created_at_datetime(self):
        """Return the created_at timestamp as a datetime object."""

        return datetime_from_epoch_ms(self.created_at)

    @property
    def last_update_datetime(self):
        """Return the last_update timestamp as a datetime object."""

        return datetime_from_epoch_ms(self.last_update)


# HACK: This is *supposed* to return a non-minified LibraryItemsResponse, but it seems to be returning a minified version instead. For now, we will use the minified response model to avoid validation errors.
class LibrarysItemsResponse(APIResponseModel):
    results: LibraryItemsResponseMinified
    total: int
    limit: int
    page: int
    sort_by: str | Missing = MISSING
    sort_desc: bool
    filter_by: str | Missing = MISSING
    media_type: MediaType
    minified: Literal[False]
    collapseseries: Literal[False]
    include: str
