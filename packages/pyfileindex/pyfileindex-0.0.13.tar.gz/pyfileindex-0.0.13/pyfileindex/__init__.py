__version__ = "0.0.1"
__all__ = []

from ._version import get_versions
from .pyfileindex import PyFileIndex

__version__ = get_versions()["version"]
del get_versions
