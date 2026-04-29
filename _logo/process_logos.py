#!/usr/bin/env python3
"""
Remove white backgrounds from logo PNGs/WEBPs and threshold to pure black.

For each input file:
  - Pixels with luminance < 128 (darker than 50% grey) AND existing alpha >= 128
    → pure black, fully opaque
  - Everything else → fully transparent

Output files are saved as <stem>_transparent.png in the same directory.

Usage:
    pip install Pillow numpy
    python3 process_logos.py
    python3 process_logos.py size_pro.png size_boomer.png   # specific files
"""

import sys
import os
from PIL import Image
import numpy as np

LOGO_DIR = os.path.dirname(os.path.abspath(__file__))

DEFAULT_FILES = [
    "size_pro.png",
    "size_boomer.png",
    "size_oldies.png",
    "junior_bw.webp",
    "junior_bq_small.webp",
]


def process(filename: str) -> None:
    src = os.path.join(LOGO_DIR, filename)
    img = Image.open(src).convert("RGBA")
    arr = np.array(img, dtype=np.float32)

    r, g, b, a = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2], arr[:, :, 3]
    luminance = 0.299 * r + 0.587 * g + 0.114 * b

    is_ink = (a >= 128) & (luminance < 128)

    out = np.zeros((arr.shape[0], arr.shape[1], 4), dtype=np.uint8)
    out[:, :, 3] = np.where(is_ink, 255, 0)

    stem = os.path.splitext(filename)[0]
    dest = os.path.join(LOGO_DIR, f"{stem}_transparent.png")
    Image.fromarray(out, "RGBA").save(dest, optimize=True)

    total = arr.shape[0] * arr.shape[1]
    print(f"{filename} ({img.size[0]}×{img.size[1]}) → {stem}_transparent.png  "
          f"({int(is_ink.sum())}/{total} opaque pixels)")


if __name__ == "__main__":
    files = sys.argv[1:] if len(sys.argv) > 1 else DEFAULT_FILES
    for f in files:
        process(f)
