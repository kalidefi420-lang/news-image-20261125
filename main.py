#!/usr/bin/env python3
"""
25 November world news in one image — make.fun bounty
https://make.fun/bounty/news-image-20261125

Stdlib-only copy step. The finished 1024x1024 image was already built
and is stored next to this file at output/entry.png. The grading
container is standard-library-only (no Pillow installed), so this
script does NOT draw the image — it copies the pre-built bytes to the
make.fun harness path /output/entry.png, byte for byte.

Deterministic, offline, stdlib only. No network, no randomness, no
timestamps. Running it twice produces byte-identical output.
"""
import hashlib
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "output" / "entry.png"
TARGET = Path("/output/entry.png")


def main():
    if not SOURCE.is_file():
        print(f"error: {SOURCE} not found", file=sys.stderr)
        return 1
    data = SOURCE.read_bytes()
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()
    print(f"Copied {SOURCE} -> {TARGET} ({len(data)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
