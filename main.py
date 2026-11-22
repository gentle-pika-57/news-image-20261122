"""Entrypoint for the make.fun news-image-20261122 competition.

The front page itself is already rendered and stored as ``entry.png``
next to this script. This program only sanity-checks that image and
places an exact byte-for-byte copy of it in the output directory, so
the shipped artifact is always the image that was reviewed. The page
covers Sunday 22 November 2026: 44 verified stories, 11 illustrated
lead stories, a dotted world map, stat boxes and a date-check strip.

Standard library only. No network, no randomness, no timestamps:
the bytes written are exactly the bytes read, so repeated runs are
byte-identical. Any failed check prints a clear message to stderr
and exits with status 1 instead of writing anything.
"""

import os
import sys
from pathlib import Path

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
MAX_SIZE_BYTES = 1048576
SOURCE_NAME = "entry.png"
OUTPUT_NAME = "entry.png"


def fail(message):
    """Print an error to stderr and exit non-zero."""
    print("error: " + message, file=sys.stderr)
    raise SystemExit(1)


def check_png(data):
    """Validate the PNG header, dimensions and size; fail otherwise."""
    if len(data) > MAX_SIZE_BYTES:
        fail(
            "entry.png is %d bytes, over the %d byte limit"
            % (len(data), MAX_SIZE_BYTES)
        )
    if len(data) < 33 or data[:8] != PNG_SIGNATURE:
        fail("entry.png does not start with the 8-byte PNG signature")
    chunk_length = int.from_bytes(data[8:12], "big")
    chunk_type = data[12:16]
    if chunk_type != b"IHDR" or chunk_length != 13:
        fail("entry.png has no valid IHDR chunk as its first chunk")
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    if width != EXPECTED_WIDTH or height != EXPECTED_HEIGHT:
        fail(
            "entry.png is %dx%d, expected %dx%d"
            % (width, height, EXPECTED_WIDTH, EXPECTED_HEIGHT)
        )


def main():
    here = Path(__file__).resolve().parent
    source = here / SOURCE_NAME
    if not source.is_file():
        fail("entry.png not found next to main.py: " + str(source))

    try:
        data = source.read_bytes()
    except OSError as exc:
        fail("could not read entry.png: " + str(exc))

    check_png(data)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    destination = Path(out_dir) / OUTPUT_NAME
    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
    except OSError as exc:
        fail("could not write output file: " + str(exc))

    print("Wrote %d bytes to %s" % (len(data), destination))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
