from importlib import import_module
import sys


def import_cache_modules(module_path: str, class_name: str):
    """The import_cache_modules function imports a module directly or from cache."""
    modules = sys.modules
    module_in_cache = not (
        module_path not in modules
        or (
            getattr(modules[module_path], "__spec__", None) is not None
            and getattr(modules[module_path].__spec__, "_initializing", False) is True
        )
    )

    if module_in_cache:
        return getattr(modules[module_path], class_name)

    import_module(module_path)


def import_module_by_path(dotted_path: str):
    """The import_module_by_path function imports a dotted module path and return the
    attribute/class designated by the last name in the path"""

    try:
        module_path, class_name = dotted_path.rsplit(".", 1)
    except ValueError as error:
        raise ImportError(f"{dotted_path} is not a module path") from error

    try:
        return import_cache_modules(module_path, class_name)
    except AttributeError as attr_err:
        raise ImportError(
            f"Module {module_path} does not define a {class_name} attribute/class"
        ) from attr_err
