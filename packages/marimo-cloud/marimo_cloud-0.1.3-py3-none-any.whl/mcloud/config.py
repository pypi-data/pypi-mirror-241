import os
from typing import List, Optional

import toml
from pydantic import BaseModel

_CREDENTIALS_FILE = "~/.marimo/credentials.toml"

DEFAULT_FILES = ["app.py", "requirements.txt", "inputs", "input", "layouts"]
REQUIRED_FILES = ["app.py"]


class Credentials(BaseModel):
    created_at: Optional[int]
    expires_at: Optional[int]
    access_token: Optional[str]
    email: Optional[str]


class AppConfiguration(BaseModel):
    app_id: Optional[str]
    app_slug: Optional[str]
    files: Optional[List[str]]


def read_credentials() -> Credentials:
    """
    Read credentials from the credentials file.
    """
    path = os.path.expanduser(_CREDENTIALS_FILE)
    try:
        with open(path, "r") as file:
            data = toml.load(file)
            return Credentials(**data)
    except FileNotFoundError:
        return Credentials()


def write_credentials(credentials: Credentials) -> None:
    """
    Write credentials to the credentials file.
    """
    path = os.path.expanduser(_CREDENTIALS_FILE)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as file:
        toml.dump(credentials.dict(), file)


def delete_credentials() -> None:
    """
    Delete the credentials file.
    """
    path = os.path.expanduser(_CREDENTIALS_FILE)
    try:
        os.remove(path)
    except FileNotFoundError:
        pass


class ConfigReader:
    def __init__(self, path: str, dryrun: bool):
        self.path = path
        self.dryrun = dryrun

    def read_app_config(self) -> AppConfiguration:
        """
        Read the app configuration from the mcloud.toml file.
        """
        file_path = os.path.join(os.getcwd(), self.path, "mcloud.toml")
        try:
            with open(file_path, "r") as file:
                data = toml.load(file)
                return AppConfiguration(**data)
        except FileNotFoundError:
            return AppConfiguration()

    def write_app_config(self, config: AppConfiguration) -> None:
        """
        Write the app configuration to the mcloud.toml file.
        """
        if self.dryrun:
            return

        path = os.path.join(os.getcwd(), self.path, "mcloud.toml")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as file:
            toml.dump(config.dict(), file)
