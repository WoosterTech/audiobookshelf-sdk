"""Created by abs_sdk.devtools.create_module."""

from pathlib import Path  # noqa: TC003
from typing import TYPE_CHECKING

from abs_sdk.core import APIResponseModel, datetime_from_epoch_ms
from abs_sdk.logging_config import get_logger

if TYPE_CHECKING:
    from datetime import datetime

logger = get_logger(__name__)


class FolderResponse(APIResponseModel):
    id: str
    full_path: Path
    library_id: str
    added_at: int

    @property
    def added_at_datetime(self) -> "datetime":
        """Return the added_at timestamp as a datetime object."""
        return datetime_from_epoch_ms(self.added_at)
