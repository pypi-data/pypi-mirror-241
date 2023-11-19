import json
import multiprocessing
import queue
from pathlib import Path

import typer
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn

from picto.utils import Snapshot, SnapshotRequest, SnapshotResult, process_bookmark_entry


def take_command(
    filepath: Path = typer.Option(
        None,
        help="The path to a bookmarks.json file as exported from a browser or a newline delimited text file of URLs",
        dir_okay=False,
        readable=True,
    ),
    url: str = typer.Option(
        None,
        help="The URL of a website you wish to take a snapshot of",
    ),
    out: Path = typer.Option(
        Path("/tmp/picto"),
        help="The output directory to store results in",
        dir_okay=True,
        writable=True,
    ),
    include_har: bool = typer.Option(
        False,
        help="Capture and save a HAR file when taking the screenshot",
    ),
    include_pdf: bool = typer.Option(
        False,
        help="Capture and save a PDF file when taking the screenshot",
    ),
    embed_har: bool = typer.Option(
        False,
        help="If true, enables include_har - save HAR in the screenshots EXIF data",
    ),
    max_processes: int = typer.Option(
        5,
        help="The number of processes to spawn which will consume the bookmarks.json entries in parallel",
    ),
    timeout: float = typer.Option(
        15.0,
        help="Wait at most this many seconds for a page to load",
    ),
    no_progress: bool = typer.Option(
        False,
        help="Disable progress bar and just print the filepaths",
    ),
):
    """
    Take a snapshot of the provided URL -
    optionally including a HAR file either as a standalone or
    embedded in the returned image as EXIF data.
    """
    progress_description: str = f"Processing bookmarks {filepath}"
    input_queue: "Queue[SnapshotRequest]" = multiprocessing.JoinableQueue()
    status_queue: "Queue[SnapshotResult]" = multiprocessing.JoinableQueue()
    stop_event = multiprocessing.Event()

    urls = {}

    if url:
        urls[url] = SnapshotRequest(url)

    if filepath is None:
        progress_description: str = f"Processing URL {url}"

        if url is None:
            max_processes = 1
            url = typer.prompt("URL to snapshot: ")
            urls[url] = SnapshotRequest(url)
    else:
        try:
            filedata = filepath.read_bytes()

            urls = {**urls, **process_bookmark_entry(json.loads(filedata))}
        except json.decoder.JSONDecodeError:
            progress_description: str = f"Processing URL List {filepath}"

            for line in filedata.decode().split("\n"):
                line = line.strip()

                if line != "":
                    urls[line] = SnapshotRequest(line)

    workers = []

    for _ in range(max_processes):
        process = multiprocessing.Process(
            target=Snapshot.worker,
            args=(
                input_queue,
                status_queue,
                stop_event,
                out,
                timeout,
                include_har,
                include_pdf,
                embed_har,
            ),
        )

        workers.append(process)

        process.start()

    for _, url_config in urls.items():
        input_queue.put(url_config)

    image_paths = []

    total = input_queue.qsize()

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        transient=True,
        disable=no_progress,
    ) as progress:
        processed_task_id = progress.add_task(
            description=progress_description,
            total=total,
        )

        while total > 0:
            try:
                result = status_queue.get(True, 0.5)
                total -= 1

                progress.update(task_id=processed_task_id, advance=1)

                if result.image_filepath is None:
                    image_paths.append(f"{result.url}")
                else:
                    image_paths.append(result.image_filepath)

                status_queue.task_done()
            except queue.Empty:
                continue

    stop_event.set()

    input_queue.join()
    status_queue.join()

    for worker in workers:
        worker.join()

    print()
    for path in image_paths:
        print(path)

    print(flush=True, end="")
