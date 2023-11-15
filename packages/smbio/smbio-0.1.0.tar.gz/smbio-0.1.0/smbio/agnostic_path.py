import os
from pathlib import Path, PureWindowsPath


class AgnosticPath(Path):
    """A class that can handle input with Windows (\\) and/or posix (/) separators for paths"""
    def __new__(cls, *args, **kwargs):
        new_path = PureWindowsPath(*args).parts
        if (os.name != "nt") and (len(new_path) > 0) and (new_path[0] in ("/", "\\")):
            new_path = ("/", *new_path[1:])
        return super().__new__(Path, *new_path, **kwargs)
