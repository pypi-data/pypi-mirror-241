import typer

from picto.cli.snapshot import SNAPSHOT
from picto import __VERSION__

cli = typer.Typer(help="Save a URL as an image - optionally embed a HAR archive of the site.")

cli.add_typer(SNAPSHOT, name="snapshot")

def version_callback(value: bool):
    if value:
        typer.echo(f"Picto Version: {__VERSION__}")
        raise typer.Exit()

@cli.callback()
def common(
    ctx: typer.Context,
    version: bool = typer.Option(None, "--version", callback=version_callback),
):
    pass

if __name__ == "__main__":
    cli()
