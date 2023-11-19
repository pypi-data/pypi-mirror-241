# Picto

Take bookmarks.json, a URL list (newline delimited), or a single URL - convert those to screenshots.

## Setup

```bash
python3 -mpip install picto
playwright install --with-deps chromium
```

## CLI

Save a URL as an image - optionally embed a HAR archive of the site.

**Usage**:

```console
$ picto [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `snapshot`

### `snapshot`

**Usage**:

```console
$ picto snapshot [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `extract`: Take a picto snapshot and extract embedded...
* `take`: Take a snapshot of the provided URL -...

#### `snapshot extract`

Take a picto snapshot and extract embedded assets

**Usage**:

```console
$ picto snapshot extract [OPTIONS]
```

**Options**:

* `--filepath FILE`: The path to a picto snapshot  [required]
* `--help`: Show this message and exit.

#### `snapshot take`

Take a snapshot of the provided URL -
optionally including a HAR file either as a standalone or
embedded in the returned image as EXIF data.

**Usage**:

```console
$ picto snapshot take [OPTIONS]
```

**Options**:

* `--filepath FILE`: The path to a bookmarks.json file as exported from a browser or a newline delimited text file of URLs
* `--url TEXT`: The URL of a website you wish to take a snapshot of
* `--out PATH`: The output directory to store results in  [default: /tmp/picto]
* `--include-har / --no-include-har`: Capture and save a HAR file when taking the screenshot  [default: no-include-har]
* `--include-pdf / --no-include-pdf`: Capture and save a PDF file when taking the screenshot  [default: no-include-pdf]
* `--embed-har / --no-embed-har`: If true, enables include_har - save HAR in the screenshots EXIF data  [default: no-embed-har]
* `--max-processes INTEGER`: The number of processes to spawn which will consume the bookmarks.json entries in parallel  [default: 5]
* `--timeout FLOAT`: Wait at most this many seconds for a page to load  [default: 15.0]
* `--no-progress / --no-no-progress`: Disable progress bar and just print the filepaths  [default: no-no-progress]
* `--help`: Show this message and exit.
