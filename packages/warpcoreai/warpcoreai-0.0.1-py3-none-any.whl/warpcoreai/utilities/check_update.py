import requests
from packaging import version

try:
    from importlib.metadata import version as get_version
except ImportError:
    from importlib_metadata import version as get_version


def check_update():
    # Fetch the latest version from the PyPI API
    response = requests.get("https://pypi.org/pypi/open-interpreter/json")
    latest_version = response.json()["info"]["version"]

    # Get the current version using importlib.metadata
    current_version = get_version("open-interpreters")

    return version.parse(latest_version) > version.parse(current_version)
