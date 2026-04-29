# _logo — Source Assets

Source logo files for the Moabiter Lastenlaufrad Kiez-WM 2026 website.
This folder is not served by Jekyll (prefix `_` excludes it from the build).
Processed outputs live in `../assets/images/`.

## Files

| File | Description |
|---|---|
| `junior_bw.webp` | Super Mighty Junior logo, B&W, large (1351×634) |
| `junior_bq_small.webp` | Super Mighty Junior logo, B&W, small (200×94) |
| `junior_bw_squares.svg` | Pixel-art squares version of the logo (vector) |
| `size_pro.png` | Kindergarten class size reference illustration |
| `size_boomer.png` | Grundschule class size reference illustration |
| `size_oldies.png` | Erwachsene class size reference illustration |
| `size comparison.png` | All three sizes side by side |
| `*_transparent.png/svg` | Processed outputs (white removed, pure black) |

## Processing script

`process_logos.py` removes white backgrounds and thresholds to pure black:

- Pixels with luminance < 50% **and** existing alpha ≥ 50% → pure black, fully opaque
- Everything else → fully transparent

### Setup

```bash
pip install Pillow numpy
```

### Run (all default files)

```bash
python3 process_logos.py
```

### Run on specific files

```bash
python3 process_logos.py size_pro.png size_boomer.png
```

Outputs are saved as `<stem>_transparent.png` in this folder.
Copy the relevant ones to `../assets/images/` to use them on the site.
