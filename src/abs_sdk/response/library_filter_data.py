"""Created by abs_sdk.devtools.create_module."""

from abs_sdk.core import APIResponseModel
from abs_sdk.logging_config import get_logger
from abs_sdk.response.author import AuthorResponseMinified  # noqa: TC001
from abs_sdk.response.series import SeriesResponseGeneric  # noqa: TC001

logger = get_logger(__name__)


class LibraryFilterDataResponse(APIResponseModel):
    """A response model representing filter data for a library.

    Note: The `series` attribute uses `SeriesResponseGeneric` to accommodate the simplified series
    response returned in the filter data, which does not include all fields of the full series response."""

    authors: list[AuthorResponseMinified]
    genres: list[str]
    tags: list[str]
    series: list[
        SeriesResponseGeneric  # this is a hack to deal with the simplified series response that is returned in the filter data, which does not include all fields of the full series response
    ]
    narrators: list[str]
    languages: list[str]
