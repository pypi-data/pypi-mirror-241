import typer

from picto.cli.snapshot import SNAPSHOT

cli = typer.Typer(help="Save a URL as an image - optionally embed a HAR archive of the site.")

cli.add_typer(SNAPSHOT, name="snapshot")

if __name__ == "__main__":
    cli()
