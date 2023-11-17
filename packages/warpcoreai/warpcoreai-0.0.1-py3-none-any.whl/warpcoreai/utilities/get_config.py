import os
import shutil
import yaml

from .local_storage_path import get_storage_path

config_filename = "config.yaml"

def get_config_path(path=None):
    """
    Gets the path to the configuration file, checking various locations or creating it if necessary.

    Args:
        path (str, optional): The path to check for the config file. Defaults to None.

    Returns:
        str: The path to the configuration file.
    """
    if path is None:
        path = os.path.join(get_storage_path(), config_filename)

    if not os.path.exists(path):
        # Check in the storage path
        storage_path = os.path.join(get_storage_path(), path)
        if os.path.exists(storage_path):
            return storage_path

        # Check in the current working directory
        cwd_path = os.path.join(os.getcwd(), path)
        if os.path.exists(cwd_path):
            return cwd_path

        # Create directory if it doesn't exist
        directory = os.path.dirname(path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        # Copy default config file
        default_config_path = os.path.join(os.path.dirname(__file__), config_filename)
        shutil.copy(default_config_path, path)

    return path


def get_config(path=None):
    """
    Reads the configuration from the given path.

    Args:
        path (str, optional): The path to the configuration file. Defaults to None.

    Returns:
        dict: The configuration data.
    """
    config_path = get_config_path(path)
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

