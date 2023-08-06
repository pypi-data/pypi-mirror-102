"""PyGPX is a python package that brings support for reading, writing and converting GPX files."""

__version__ = "0.0.1"  # noqa


class GPX:
    """A GPX class for the GPS Exchange Format (GPX) data format.

    Args:
        file (str): The path to the GPX file.
    """

    def __init__(self, file: str) -> None:
        self._file = file
