import os
import tarfile
from typing import List

from rich.console import Console

import mcloud.prompter as prompter
from mcloud.client import create_marimo_client
from mcloud.config import DEFAULT_FILES, REQUIRED_FILES, ConfigReader
from mcloud.generated import CreateApplicationRequest

console = Console()

ASSETS_NAME = "app_source.tar.gz"


def read_app_py(path: str) -> str:
    """
    Read app.py from current directory

    TODO: make location configurable
    """
    try:
        file_path = os.path.join(os.getcwd(), path, "app.py")
        with open(file_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        directory = os.path.join(os.getcwd(), path)
        raise Exception(f"app.py not found in {directory}") from None


def read_requirements_txt(path: str) -> str:
    """
    Read requirements.txt from current directory

    TODO: make location configurable
    """
    try:
        file_path = os.path.join(os.getcwd(), path, "requirements.txt")
        with open(file_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def publish(
    path: str,
    dryrun: bool,
) -> None:
    """
    Publish current directory to Marimo
    """
    # Create client
    client = create_marimo_client(dryrun=dryrun)
    # Read app config
    config_reader = ConfigReader(path, dryrun)
    app_config = config_reader.read_app_config()

    # If no app id, ask to link app
    if not app_config.app_id:
        # Ask to link app or create new
        link_or_new = prompter.select(
            "No application linked. Would you like to link an existing application or create a new one?",
            ["Link existing", "Create new", "Cancel"],
        )

        # If cancel, exit
        if link_or_new == "Cancel":
            return
        # If link existing, ask for app id
        elif link_or_new == "Link existing":
            # Select organizations
            orgs = client.list_organizations()
            if len(orgs) == 0:
                console.print("[red]No organizations found[/red]")
                return
            selected_org = prompter.select(
                "Select organization",
                orgs,
                lambda org: org.organization_slug,
            )

            # Select app
            apps = client.list_applications(
                organization_id=selected_org.organization_id
            )
            if len(apps) == 0:
                console.print("[red]No applications found[/red]")
                return
            selected_app = prompter.select(
                "Select application",
                apps,
                lambda app: f"{app.name} ({app.application_slug})",
            )
        # If create new, ask for app name
        elif link_or_new == "Create new":
            # Select organizations
            orgs = client.list_organizations()
            if len(orgs) == 0:
                console.print("[red]No organizations found[/red]")
                return
            selected_org = prompter.select(
                "Select organization",
                orgs,
                lambda org: org.organization_slug,
            )

            # Ask for app name
            app_name = prompter.text("Enter a name for your application")

            # Ask for app slug
            app_slug = prompter.slug(
                "Enter a slug for your application", default=app_name
            )

            # Create app
            selected_app = client.create_application(
                request=CreateApplicationRequest(
                    application_slug=app_slug,
                    name=app_name,
                    organization_id=selected_org.organization_id,
                )
            )
        else:
            raise Exception("Invalid option selected")

        # Save app id
        app_config.app_id = selected_app.application_id
        app_config.app_slug = selected_app.application_slug
        config_reader.write_app_config(app_config)

    else:
        # Load app
        app = client.get_application(application_id=app_config.app_id)

        # If slug doesn't match, write new slug its only used for display
        if app.application_slug != app_config.app_slug:
            app_config.app_slug = app.application_slug
            config_reader.write_app_config(app_config)

        # Confirm app
        confirm = prompter.confirm(
            f"Deploy application [cyan bold]{app.application_slug}[/cyan bold]?"
        )

        if not confirm:
            return

    # Read app.py and requirements.txt
    code = read_app_py(path)
    requirements = read_requirements_txt(path)
    assets = _tar_assets(path, app_config.files or DEFAULT_FILES, REQUIRED_FILES)

    with console.status(
        f"[cyan]Deploying [bold]{app_config.app_slug}[/bold]...[/cyan]"
    ):
        # Start deployment
        try:
            response = client.create_deployment(
                application_id=app_config.app_id,
                code=code,
                requirements_txt=requirements,
                assets=assets,
            )
            # TODO: link to deployment when we support that page
            deployment_url = (
                f"https://marimo.io/dashboard/applications/{response.application_id}"
            )
            console.print("[green]Application deployed![/green]")
            console.print(f"View your application at [cyan]{deployment_url}[/cyan]")
        except Exception as e:
            console.print(f"[red]Error deploying application: {e}[/red]")
            raise e
        finally:
            # delete tar file
            assets.close()
            os.remove(ASSETS_NAME)


def _tar_assets(
    path: str,
    files: List[str],
    required_files: List[str],
) -> tarfile.TarFile:
    """
    Tar all the assets in the current directory and return the tar file.
    """

    # Create tar file
    tar = tarfile.open(ASSETS_NAME, "w:gz")
    for file in files:
        file_path = os.path.join(os.getcwd(), path, file)
        if not os.path.exists(file_path):
            if file in required_files:
                raise Exception(f"Required file {file} not found")
            else:
                continue
        tar.add(file_path, arcname=os.path.join("app_source", file))
    # Close tar file
    tar.close()

    # Return tar file
    return open(ASSETS_NAME, "rb")
