"""Created by abs_sdk.devtools.create_module."""

from functools import cached_property
from typing import TYPE_CHECKING

from attrmagic.sentinels import MISSING, Missing

from abs_sdk.core import APIResponseModel, datetime_from_epoch_ms
from abs_sdk.logging_config import get_logger

if TYPE_CHECKING:
    import datetime as dt

logger = get_logger(__name__)


class _AuthorResponseBase(APIResponseModel):
    id: str
    name: str


class AuthorResponse(_AuthorResponseBase):
    asin: str | None
    description: str | None
    image_path: str | None
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


class AuthorResponseMinified(_AuthorResponseBase):
    """A minified version of the AuthorResponse model, containing only essential fields."""


class AuthorResponseExpanded(AuthorResponse):
    """An expanded version of the AuthorResponse model, potentially including additional fields or relationships."""

    num_books: int


class AuthorResponseGeneric(_AuthorResponseBase):
    """A generic version of the AuthorResponse model, which can be used for various purposes where a specific response type is not required."""

    asin: str | None | Missing = MISSING
    description: str | None | Missing = MISSING
    image_path: str | None | Missing = MISSING
    added_at: int | Missing = MISSING
    updated_at: int | Missing = MISSING
    num_books: int | Missing = MISSING

    @cached_property
    def added_at_datetime(self) -> "dt.datetime | Missing":
        """Convert the added_at timestamp to a datetime object."""
        if self.added_at is MISSING:
            return MISSING
        return datetime_from_epoch_ms(self.added_at)

    @cached_property
    def updated_at_datetime(self) -> "dt.datetime | Missing":
        """Convert the updated_at timestamp to a datetime object."""
        if self.updated_at is MISSING:
            return MISSING
        return datetime_from_epoch_ms(self.updated_at)
