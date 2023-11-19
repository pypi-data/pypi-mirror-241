from pathlib import Path

import typer

from picto.utils import Snapshot


def extract_command(
    filepath: Path = typer.Option(
        ...,
        help="The path to a picto snapshot",
        dir_okay=False,
        readable=True,
    ),
):
    """
    Take a picto snapshot and extract embedded assets
    """
    har_filepath, url = Snapshot.extract(filepath)

    if har_filepath and har_filepath.exists():
        print(f"{url}|{har_filepath}")
    else:
        print(f"Failed to extract any assets from: {filepath}")
