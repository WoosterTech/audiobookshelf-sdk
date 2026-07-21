"""Created by abs_sdk.devtools.create_module."""

from typing import Annotated

from attrmagic.sentinels import MISSING, Missing
from pydantic import Field

from abs_sdk.core import APIResponseModel
from abs_sdk.logging_config import get_logger
from abs_sdk.response.author import AuthorResponseMinified  # noqa: TC001
from abs_sdk.response.series import SeriesResponseSequence  # noqa: TC001

logger = get_logger(__name__)


class _BookMetadataResponseBase(APIResponseModel):
    title: str | None
    subtitle: str | None
    genres: list[str]
    published_year: str | None
    published_date: str | None
    publisher: str | None
    description: str | None
    isbn: str | None
    asin: str | None
    language: str | None
    explicit: bool


class BookMetadataResponse(_BookMetadataResponseBase):
    """A response model for book metadata, containing detailed information about a book."""

    authors: list[AuthorResponseMinified]
    narrators: list[str]
    series: list[SeriesResponseSequence]


class _BookMetadataResponseCommon(_BookMetadataResponseBase):
    """A common response model for book metadata, containing shared fields across different book metadata responses."""

    title_ignore_prefix: str
    author_name: str
    author_name_lf: Annotated[str, Field(alias="authorNameLF")]
    narrator_name: str
    series_name: str


class BookMetadataResponseMinified(_BookMetadataResponseCommon):
    """A minified version of the BookMetadataResponse model, containing only essential fields for quick access."""

    pass


class BookMetadataResponseExpanded(BookMetadataResponse, _BookMetadataResponseCommon):
    """An expanded version of the BookMetadataResponse model, potentially including additional fields or relationships."""

    pass


class BookMetadataResponseGeneric(_BookMetadataResponseBase):
    """A generic version of the BookMetadataResponse model, which can be used for various purposes where a specific response type is not required."""

    authors: list[AuthorResponseMinified] | Missing = MISSING
    narrators: list[str] | Missing = MISSING
    series: list[SeriesResponseSequence] | Missing = MISSING

    title_ignore_prefix: str | Missing = MISSING
    author_name: str | Missing = MISSING
    author_name_lf: Annotated[str | Missing, Field(alias="authorNameLF")] = MISSING
    narrator_name: str | Missing = MISSING
    series_name: str | Missing = MISSING
