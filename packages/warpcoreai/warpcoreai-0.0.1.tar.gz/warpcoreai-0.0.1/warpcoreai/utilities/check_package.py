import importlib.util
import sys


def check_package(package):
    """
    Check if a package is available in the system and try to import it if it is.

    Args:
    package (str): The name of the package to check and import.

    Returns:
    bool: True if the package is available and successfully imported, False otherwise.
    """
    if package in sys.modules:
        return True

    spec = importlib.util.find_spec(package)
    if spec is not None:
        try:
            module = importlib.util.module_from_spec(spec)
            sys.modules[package] = module
            spec.loader.exec_module(module)
            return True
        except ImportError:
            # Handle the specific import error if needed
            return False
    else:
        return False
