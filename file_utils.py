"""Helpers for reading benchmark text files with legacy encoding support."""

from contextlib import contextmanager
from io import StringIO
from os import PathLike
from typing import Iterator, Optional, TextIO, Union


Pathish = Union[str, PathLike[str]]


def read_file_with_fallback(path: Pathish) -> str:
    """Read *path* as UTF-8, falling back to Windows CP1252."""
    try:
        with open(path, "r", encoding="utf-8") as file_handler:
            return file_handler.read()
    except UnicodeDecodeError:
        with open(path, "r", encoding="cp1252") as file_handler:
            return file_handler.read()


@contextmanager
def open_file_with_fallback(path: Pathish, *, newline: Optional[str] = None) -> Iterator[TextIO]:
    """Open decoded text for parsers that require a file-like object."""
    with StringIO(read_file_with_fallback(path), newline=newline) as file_handler:
        yield file_handler
