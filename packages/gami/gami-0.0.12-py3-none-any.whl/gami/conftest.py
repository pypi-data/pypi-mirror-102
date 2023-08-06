import tempfile
from shutil import rmtree
from contextlib import contextmanager


@contextmanager
def ensure_clean_dir():
    """
    Get a temporary directory path and agrees to remove on close.
    Yields
    ------
    Temporary directory path
    """
    directory_name = tempfile.mkdtemp(suffix="")
    try:
        yield directory_name
    finally:
        try:
            rmtree(directory_name)
        except OSError:
            pass
