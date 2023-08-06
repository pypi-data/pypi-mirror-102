#  Copyright (c) 2021  SBA - MIT License

from .bin_tree import BinTree


def _get_version():
    try:
        from .version import version
    except ImportError:
        version = '0.0.0'
    return version


__version__ = _get_version()
