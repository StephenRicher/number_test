try:
    from importlib.metadata import version
    __version__ = version("number_test")
except ModuleNotFoundError:
    __version__ = '0.1.0' # Required for python 3.7 compatibility
