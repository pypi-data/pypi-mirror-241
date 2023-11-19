import importlib.metadata

from .connection import Connection
from .cursor import Cursor

__version__ = importlib.metadata.version("tipsql-sqlite3")

__all__ = ["__version__", "Connection", "Cursor"]
