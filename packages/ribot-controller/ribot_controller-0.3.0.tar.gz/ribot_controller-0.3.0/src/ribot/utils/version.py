import requests
from packaging import version
import os

def get_version(*args,**kwargs) -> str:
    url = "https://pypi.org/pypi/ribot-controller/json"

    test_var = os.environ.get("TEST_VAR",'NOt set:()')
    print(f"TEST_VAR: {test_var}")


    response = requests.get(url)
    if response.status_code == 200:
        package_info = response.json()
        current_version_str = package_info["info"]["version"]

        # Parse the version string
        current_version = version.parse(current_version_str)
        print(f"Current version: {current_version}")

        # Increment the minor version
        new_version = version.Version(f"{current_version.major}.{current_version.minor + 1}.{current_version.micro}")

        return str(new_version)
    else:
        raise Exception("Failed to retrieve package information")


