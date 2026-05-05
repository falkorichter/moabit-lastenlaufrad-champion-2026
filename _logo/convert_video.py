#!/usr/bin/env python3
"""
convert_video.py — Prepare a video for web embedding (autoplay loop).

Outputs:
  assets/videos/<slug>.mp4   — H.264, web-optimised (faststart, max 780px wide)
  assets/videos/<slug>.webm  — VP9, smaller for Chrome/Firefox

Usage:
  python3 _logo/convert_video.py <input_video> <output_slug>

Example:
  python3 _logo/convert_video.py /path/to/clip.mp4 foto-pins-timelapse

Paste the printed HTML snippet into a _posts/*.md file.
Requires: ffmpeg (brew install ffmpeg)
"""

import subprocess
import sys
import os

MAX_WIDTH = 780


def convert(src: str, slug: str) -> None:
    out_dir = os.path.join(os.path.dirname(__file__), '..', 'assets', 'videos')
    os.makedirs(out_dir, exist_ok=True)

    mp4  = os.path.join(out_dir, f'{slug}.mp4')
    webm = os.path.join(out_dir, f'{slug}.webm')

    scale = f'scale=min({MAX_WIDTH}\\,iw):-2'

    print(f'→ encoding MP4 …')
    subprocess.run([
        'ffmpeg', '-y', '-i', src,
        '-vf', scale,
        '-c:v', 'libx264', '-crf', '23', '-preset', 'slow',
        '-pix_fmt', 'yuv420p',
        '-movflags', '+faststart',
        '-an',
        mp4,
    ], check=True)

    print(f'→ encoding WebM …')
    subprocess.run([
        'ffmpeg', '-y', '-i', src,
        '-vf', scale,
        '-c:v', 'libvpx-vp9', '-crf', '33', '-b:v', '0',
        '-an',
        webm,
    ], check=True)

    mp4_kb  = os.path.getsize(mp4)  // 1024
    webm_kb = os.path.getsize(webm) // 1024
    print(f'\nDone.')
    print(f'  MP4:  assets/videos/{slug}.mp4   ({mp4_kb} KB)')
    print(f'  WebM: assets/videos/{slug}.webm  ({webm_kb} KB)')
    print(f'\nHTML snippet:\n')
    print(f'<video autoplay loop muted playsinline style="width:100%;height:auto;border-radius:12px;margin-top:1.2rem;">')
    print(f'  <source src="/assets/videos/{slug}.webm" type="video/webm">')
    print(f'  <source src="/assets/videos/{slug}.mp4"  type="video/mp4">')
    print(f'</video>')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2])
