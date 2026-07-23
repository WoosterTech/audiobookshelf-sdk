from __future__ import annotations

import os
from pathlib import Path

import pytest


def _parse_env_line(line: str) -> tuple[str, str] | None:
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return None

    if stripped.startswith("export "):
        stripped = stripped[7:].lstrip()

    if "=" not in stripped:
        return None

    key, value = stripped.split("=", 1)
    key = key.strip()
    value = value.strip()
    if not key:
        return None

    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        value = value[1:-1]

    return key, value


def _load_env_file(path: Path) -> None:
    if not path.exists() or not path.is_file():
        return

    for line in path.read_text(encoding="utf-8").splitlines():
        parsed = _parse_env_line(line)
        if parsed is None:
            continue
        key, value = parsed
        _ = os.environ.setdefault(key, value)


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--run-functional",
        action="store_true",
        default=False,
        help="Run functional tests that call a real Audiobookshelf server.",
    )
    parser.addoption(
        "--functional-env-file",
        action="store",
        default=".env.functional",
        help=(
            "Path to an optional env file loaded for functional tests. "
            "Existing environment variables always win."
        ),
    )


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line(
        "markers",
        "functional: marks tests that call a real Audiobookshelf server",
    )

    if config.getoption("--run-functional"):
        env_file = Path(config.getoption("--functional-env-file"))  # pyright: ignore[reportArgumentType]
        _load_env_file(env_file)


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    if config.getoption("--run-functional"):
        return

    skip_functional = pytest.mark.skip(
        reason="use --run-functional to run real-server functional tests"
    )
    for item in items:
        if "functional" in item.keywords:
            item.add_marker(skip_functional)
