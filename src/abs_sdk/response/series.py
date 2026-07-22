"""Created by abs_sdk.devtools.create_module."""

from functools import cached_property
from typing import TYPE_CHECKING

from attrmagic.sentinels import MISSING, Missing

from abs_sdk.core import APIResponseModel, datetime_from_epoch_ms
from abs_sdk.logging_config import get_logger

if TYPE_CHECKING:
    import datetime as dt

logger = get_logger(__name__)


class _SeriesResponseBase(APIResponseModel):
    id: str
    name: str


class SeriesResponse(_SeriesResponseBase):
    description: str | None
    added_at: int
    updated_at: int

    @cached_property
    def added_at_datetime(self) -> "dt.datetime":
        """Convert the added_at timestamp to a datetime object."""
        return datetime_from_epoch_ms(self.added_at)

    @cached_property
    def updated_at_datetime(self) -> "dt.datetime":
        """Convert the updated_at timestamp to a datetime object."""
        return datetime_from_epoch_ms(self.updated_at)


class SeriesResponseSequence(_SeriesResponseBase):
    sequence: str | None


class SeriesResponseGeneric(_SeriesResponseBase):
    """A generic version of the SeriesResponse model, which can be used for various purposes where a specific response type is not required."""

    description: str | None | Missing = MISSING
    added_at: int | Missing = MISSING
    updated_at: int | Missing = MISSING
    sequence: str | None | Missing = MISSING

    @cached_property
    def added_at_datetime(self) -> "dt.datetime | Missing":
        """Convert the added_at timestamp to a datetime object, if available."""
        if self.added_at is not MISSING:
            return datetime_from_epoch_ms(self.added_at)
        return MISSING

    @cached_property
    def updated_at_datetime(self) -> "dt.datetime | Missing":
        """Convert the updated_at timestamp to a datetime object, if available."""
        if self.updated_at is not MISSING:
            return datetime_from_epoch_ms(self.updated_at)
        return MISSING
