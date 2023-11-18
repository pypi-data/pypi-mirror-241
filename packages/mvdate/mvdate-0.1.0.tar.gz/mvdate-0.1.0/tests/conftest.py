"""Configure fixtures for tests."""
from pathlib import Path

import pytest


@pytest.fixture()
def test_file(tmp_path: Path) -> Path:
    """Create a temporary file and return its Path."""
    _file = tmp_path / "test.txt"
    _file.touch()
    return _file


@pytest.fixture()
def test_jpg() -> Path:
    """Return path to a sample JPG image."""
    return Path("tests/resources/sample.jpg")
