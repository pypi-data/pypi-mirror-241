import requests
from packaging import version

def get_version() -> str:
    url = "https://pypi.org/pypi/ribot-controller/json"

    response = requests.get(url)
    if response.status_code == 200:
        package_info = response.json()
        current_version_str = package_info["info"]["version"]

        # Parse the version string
        current_version = version.parse(current_version_str)

        # Increment the minor version
        new_version = version.Version(f"{current_version.major}.{current_version.minor + 1}.{current_version.micro}")

        return str(new_version)
    else:
        raise Exception("Failed to retrieve package information")

# Example usage
new_version = get_version()
print(f"New version: {new_version}")

