"""Created by abs_sdk.devtools.create_module."""

from attrmagic.sentinels import MISSING, Missing

from abs_sdk.core import APIResponseModel, datetime_from_epoch_ms
from abs_sdk.logging_config import get_logger
from abs_sdk.response.library_item import LibraryItemResponseMinified
from abs_sdk.response.podcast_episode import PodcastEpisodeResponse  # noqa: TC001

logger = get_logger(__name__)


class LibraryItemResponseMinifiedExtended(LibraryItemResponseMinified):
    """A response model representing a minified library item with additional fields."""

    progress_last_update: int
    recent_episode: PodcastEpisodeResponse | Missing = MISSING

    @property
    def progress_last_update_datetime(self):
        """Return the progress last update as a datetime object."""

        return datetime_from_epoch_ms(self.progress_last_update)


class ItemsInProgressResponse(APIResponseModel):
    library_items: list[LibraryItemResponseMinifiedExtended]
