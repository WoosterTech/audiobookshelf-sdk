"""Created by abs_sdk.devtools.create_module."""

from abs_sdk.core import APIResponseModel
from abs_sdk.logging_config import get_logger

logger = get_logger(__name__)


class LibrarySettingsResponse(APIResponseModel):
    """Represents the settings of a library."""

    cover_aspect_ratio: int
    disable_watcher: bool
    skip_matching_media_with_asin: bool
    skip_matching_media_with_isbn: bool
    auto_scan_cron_expression: str | None

    @property
    def square_cover(self) -> bool:
        """Determine if the cover aspect ratio indicates a square cover."""
        return self.cover_aspect_ratio == 1
