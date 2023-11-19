import typer

from picto.cli.snapshot.take import take_command
from picto.cli.snapshot.extract import extract_command
from picto.utils import Snapshot

SNAPSHOT = typer.Typer()

SNAPSHOT.command(name="take")(take_command)
SNAPSHOT.command(name="extract")(extract_command)
