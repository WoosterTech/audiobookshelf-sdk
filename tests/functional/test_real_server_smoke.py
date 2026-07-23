from __future__ import annotations

import os
from typing import TYPE_CHECKING

import pytest

from abs_sdk import AudiobookshelfClient

if TYPE_CHECKING:
    from collections.abc import Iterator


def _get_required_env(name: str) -> str:
    value = os.getenv(name)
    if value:
        return value
    pytest.skip(f"missing required env var: {name}")


def _get_verify_ssl() -> bool:
    raw_value = os.getenv("AUDIOBOOKSHELF_TEST_VERIFY_SSL", "true").strip().lower()
    return raw_value not in {"0", "false", "no", "off"}


@pytest.fixture
def client() -> Iterator[AudiobookshelfClient]:
    base_url = _get_required_env("AUDIOBOOKSHELF_TEST_BASE_URL")
    token = _get_required_env("AUDIOBOOKSHELF_TEST_TOKEN")

    with AudiobookshelfClient(
        base_url=base_url, token=token, verify_ssl=_get_verify_ssl()
    ) as api_client:
        yield api_client


@pytest.mark.functional
def test_can_read_libraries(client: AudiobookshelfClient) -> None:
    libraries = client.libraries.get_all_libraries()
    assert isinstance(libraries.libraries, list)
    assert len(libraries.libraries) > 0


@pytest.mark.functional
def test_can_read_me_items_in_progress(client: AudiobookshelfClient) -> None:
    items = client.me.get_library_items_in_progress(limit=5)
    assert isinstance(items.library_items, list)


@pytest.mark.functional
def test_can_read_specific_library_and_items(client: AudiobookshelfClient) -> None:
    configured_library_id = os.getenv("AUDIOBOOKSHELF_TEST_LIBRARY_ID")

    if configured_library_id is None:
        libraries = client.libraries.get_all_libraries()
        if not libraries.libraries:
            pytest.skip("no libraries available for this user")
        configured_library_id = str(libraries.libraries[0].id)

    library = client.libraries.get_a_library(configured_library_id)
    assert str(library.id) == configured_library_id

    items_page = client.libraries.get_library_items(configured_library_id, limit=3, page=0)
    assert items_page.limit >= 0
    assert isinstance(items_page.results.root, list)
