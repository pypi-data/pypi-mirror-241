import typer
from rich.console import Console
from typing_extensions import Annotated

import mcloud.auth as marimo_auth
import mcloud.publish as marimo_publish

console = Console()
app = typer.Typer(
    pretty_exceptions_show_locals=False,
    pretty_exceptions_short=True,
)

__version__ = "0.2.0"


@app.command()
def version():
    console.print(__version__)


@app.command()
def login():
    marimo_auth.login()


@app.command()
def publish(
    path: Annotated[
        str, typer.Argument(..., help="Path to the directory to publish")
    ] = ".",
    dryrun: Annotated[bool, typer.Option(help="Dry run")] = False,
):
    marimo_publish.publish(
        path=path,
        dryrun=dryrun,
    )


@app.command()
def logout():
    marimo_auth.logout()


if __name__ == "__main__":
    app()
