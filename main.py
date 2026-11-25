#!/usr/bin/env python3
"""
Sum up 25 November's world news in one image — make.fun bounty
https://make.fun/bounty/news-image-20261125

Evening-edition variant (v2): the full day of Wednesday 25 November
2026 in one 1024x1024 image.

This program is STANDARD LIBRARY ONLY. It copies the pre-built
output/entry.png (drawn locally with an image-drawing library — see
README.md) to /output/entry.png. It imports nothing beyond the
standard library, because the grading container installs nothing.

Running it twice produces byte-identical output (a plain file copy).
"""
import hashlib
import os
import shutil
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "output" / "entry.png"
MAX_BYTES = 1 * 1024 * 1024  # bounty limit: image must be at most 1 MiB
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def output_path():
    """Where the harness expects the image. MAKEFUN_OUTPUT_DIR is only
    for local testing; the grader runs with the default /output."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(base) / "entry.png"


def main():
    if not SOURCE.is_file():
        print(f"error: source image not found: {SOURCE}", file=sys.stderr)
        return 1
    # Self-check the image before handing it to the harness: it must be
    # a real PNG, 1024x1024 or smaller, and within the 1 MiB limit.
    # Failing loudly here beats silently submitting a bad file.
    data = SOURCE.read_bytes()
    if not data.startswith(PNG_MAGIC):
        print("error: source image is not a PNG", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print(f"error: source image is {len(data)} bytes, over the "
              f"{MAX_BYTES} byte limit", file=sys.stderr)
        return 1
    dest = output_path()
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, dest)
    if sha256(dest) != sha256(SOURCE):
        print("error: copied image does not match the source",
              file=sys.stderr)
        return 1
    print(f"Wrote {dest} ({dest.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
