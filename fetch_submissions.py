#!/usr/bin/env python3
"""
Fetch form submissions from formsubmit.co and write to submissions.csv.

Requires .env with FORMSUBMIT_API_KEY (max 5 calls/day, data kept 30 days).

Usage:
    python3 fetch_submissions.py
"""

import csv
import json
import os
import urllib.request
from pathlib import Path

env = Path(__file__).parent / ".env"
for line in env.read_text().splitlines():
    if "=" in line and not line.startswith("#"):
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip())

api_key = os.environ.get("FORMSUBMIT_API_KEY")
if not api_key:
    raise SystemExit("FORMSUBMIT_API_KEY not set — check your .env file")

url = f"https://formsubmit.co/api/get-submissions/{api_key}"
with urllib.request.urlopen(url) as r:
    data = json.load(r)

submissions = data["submissions"]
out_path = Path(__file__).parent / "submissions.csv"

with open(out_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["submitted_at", "name", "email", "phone", "klasse", "message"])
    for s in submissions:
        fd = s["form_data"]
        writer.writerow([
            s["submitted_at"]["date"],
            fd.get("name", ""),
            fd.get("email", ""),
            fd.get("phone") or "",
            fd.get("klasse", ""),
            fd.get("message") or "",
        ])

print(f"✓ {len(submissions)} submissions written to {out_path}")
