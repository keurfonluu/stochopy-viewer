try:
    from importlib import metadata
except ImportError:
    import importlib_metadata as metadata

try:
    __version__ = metadata.version("stochopy-viewer")
except Exception:
    __version__ = "unknown"
