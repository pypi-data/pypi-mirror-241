import multiprocessing
import os
import queue
import shutil
from dataclasses import dataclass
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Union
from urllib.parse import urlparse

from PIL import Image as PillowImage
from playwright.sync_api import Browser, sync_playwright
from slugify import slugify

PillowImage.MAX_IMAGE_PIXELS = 933120000

@dataclass
class SnapshotRequest:
    """Class for keeping track of URLs to snapshot"""

    url: str
    title: str = ""


@dataclass
class SnapshotResult:
    """Class for keeping track of URLs to snapshot results"""

    url: str
    image_filepath: Path
    pdf_filepath: Path = None
    har_filepath: Path = None


def process_bookmark_entry(node):
    """
    process_bookmark_entry
    """
    bookmarks = {}

    for key, value in node.items():
        if key == "uri":
            bookmarks[value] = SnapshotRequest(
                url=value,
                title=node.get("title", ""),
            )

        if key == "children":
            for node in value:
                bookmarks = {**bookmarks, **process_bookmark_entry(node)}

    return bookmarks


class Snapshot:
    """
    Snapshot
    """

    EXIF_TAG_HAR = 1024
    EXIF_TAG_URL = 1025

    @classmethod
    def extract(cls, filepath: Path):
        """
        extract assets from a picto snapshot
        """
        pillow_img = PillowImage.open(str(filepath))
        img_exif = pillow_img.getexif()

        har_data = img_exif.get(cls.EXIF_TAG_HAR, False)
        url = img_exif.get(cls.EXIF_TAG_URL, b"").decode()
        name = filepath.stem
        ret = False

        if har_data:
            ret = filepath.parent.joinpath(slugify(f"{name}")).with_suffix(".har")

            with open(ret, mode="wb") as fh:
                fh.write(har_data)

        return ret, url

    @classmethod
    def worker(
        cls,
        input_queue: multiprocessing.JoinableQueue,
        status_queue: multiprocessing.JoinableQueue,
        stop_event: multiprocessing.Event,
        basepath: Path,
        timeout: float = 15.0,
        include_har: bool = False,
        include_pdf: bool = False,
        embed_har: bool = False,
    ):
        """
        worker
        """
        basepath.mkdir(exist_ok=True, parents=True)

        with sync_playwright() as playwright:
            for browser_type in [playwright.chromium]:
                browser = browser_type.launch()

            while not stop_event.is_set():
                try:
                    # Check if any URL has arrived in the input queue. If not,
                    # loop back and try again.
                    url_config = input_queue.get(True, 1)

                    image_filepath, har_filepath = cls.url(
                        browser,
                        url_config.url,
                        basepath,
                        title=url_config.title,
                        timeout=timeout,
                        include_har=include_har,
                        include_pdf=include_pdf,
                        embed_har=embed_har,
                    )

                    status_queue.put(
                        SnapshotResult(
                            url=url_config.url,
                            image_filepath=image_filepath,
                            har_filepath=har_filepath,
                        )
                    )
                    input_queue.task_done()
                except queue.Empty:
                    continue

            browser.close()

    @classmethod
    def url(
        cls,
        browser: Union[Browser, None],
        url: str,
        basepath: Path,
        title: str = "",
        timeout: float = 15.0,
        include_har: bool = True,
        include_pdf: bool = False,
        embed_har: bool = False,
    ):
        """
        url
        """
        context_options = {
            "ignore_https_errors": True,
        }

        pdf_filepath = False
        png_filepath = False
        har_filepath = False

        if browser is None:
            playwright = sync_playwright().start()
            chrome = playwright.chromium
            browser = chrome.launch()

        if include_har or embed_har:
            context_options["record_har_path"] = NamedTemporaryFile(mode="wb", delete=False).name

        with NamedTemporaryFile(mode="wb") as fh:
            context = browser.new_context(**context_options)

            page = context.new_page()

            page.set_viewport_size({"width": 1920, "height": 1080})

            page.emulate_media(media="screen")

            page.goto(url, timeout=timeout * 1000, wait_until="domcontentloaded")

            title = title.strip()

            if title == "":
                urlbase = urlparse(url)
                basepath = basepath.joinpath(urlbase.hostname)
                basepath.mkdir(parents=True, exist_ok=True)
                title = f"{urlbase.path}-{page.title()}"

            title = slugify(title)

            namemax = os.pathconf(basepath, 'PC_NAME_MAX')

            if namemax > 0:
                title = title[0:namemax-5]

            filename = basepath.joinpath(title)

            pdf_filepath = filename.with_suffix(".pdf")
            png_filepath = filename.with_suffix(".png")
            har_filepath = filename.with_suffix(".har")

            if include_pdf:
                page.pdf(
                    path=pdf_filepath,
                    prefer_css_page_size=True,
                    print_background=True,
                )

            page.screenshot(path=fh.name, full_page=True)

            context.close()

            pillow_img = PillowImage.open(fh.name)
            img_exif = pillow_img.getexif()

            har_data = b""

            if embed_har:
                shutil.copyfile(context_options["record_har_path"], str(har_filepath))
                har_data = har_filepath.read_bytes()
                har_filepath.unlink(missing_ok=True)

            img_exif[cls.EXIF_TAG_HAR] = har_data
            img_exif[cls.EXIF_TAG_URL] = bytes(url, "utf8")

            pillow_img.save(png_filepath, exif=img_exif)

        return (png_filepath, har_filepath)
