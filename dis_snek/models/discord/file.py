from io import IOBase
from pathlib import Path
from typing import Optional, Union

from dis_snek.client.utils.attr_utils import define, field

__all__ = ["File", "open_file"]


@define(kw_only=False)
class File:
    """
    Representation of a file.

    Used to

    """

    file: Union["IOBase", "Path", str] = field(repr=True)
    """Location of file to send or the bytes."""
    file_name: Optional[str] = field(repr=True, default=None)
    """Set a filename that will be displayed when uploaded to discord. If you leave this empty, the file will be called `file` by default"""

    def open_file(self) -> "IOBase":
        if isinstance(self.file, IOBase):
            return self.file
        else:
            return open(str(self.file), "rb")


def open_file(file: Union[File, "IOBase", "Path", str]) -> IOBase:
    match file:
        case File():
            return file.open_file()
        case IOBase():
            return file
        case Path() | str():
            return open(str(file), "rb")
        case _:
            raise ValueError(f"{file} is not a valid file")
