# Moabiter Lastenlaufrad Kiez-Weltmeisterschaft 2026

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

Website for the first Moabiter Lastenlaufrad Kiez-WM, hosted at **[moabit.pimpmycargo.bike](https://moabit.pimpmycargo.bike)**.

This repo is designed to be a **reusable blueprint** for future community events — see the sections below for how each feature works.

---

## Event details

| | |
|---|---|
| **Date** | 9. Mai 2026, 16:00 Uhr |
| **Location** | Zazza Frühlingsfest, Moabit, Berlin |
| **Instagram** | [@zazza_moabit](https://www.instagram.com/zazza_moabit/) |
| **Contact** | moabit-2026@pimpmycargo.bike |
| **Organiser** | Falko Richter / [PimpMyCargo.bike](https://www.pimpmycargo.bike) — [@pimpmycargo.bike](https://www.instagram.com/pimpmycargo.bike/) |
| **Partners** | [Super Bicycles](https://super-bicycles.com), [Zazza Moabit](https://www.pajas-kaffee.de/about-3) |

### Classes

| Class | Nickname |
|---|---|
| Kindergarten | Die Pros |
| Grundschule | Lauf-Boomer |
| Erwachsene | Oldies |

Official race bike: [Super Mighty Junior – Cargo-Laufrad](https://super-bicycles.com/products/super-mighty-junior-cargo-laufrad) by Super Bicycles. Participants bring their own helmet; gloves recommended.

---

## Tech stack

- **[Jekyll](https://jekyllrb.com/) 4.x** static site — no framework, no JS build step
- **GitHub Pages** with custom domain; CNAME at [united-domains.de](https://www.united-domains.de/) → `falkorichter.github.io`
- **[formsubmit.co](https://formsubmit.co)** — no-backend registration form
- **No cookies, no tracking** — plain HTML/CSS/JS, DSGVO-compliant

---

## Project structure

```
moabit-2026/
├── _config.yml               # Site title, description, URL
├── _layouts/
│   ├── default.html          # Base layout: OG tags, footer, imprint, JS
│   └── post.html             # Blog post wrapper
├── _posts/                   # Blog posts (YYYY-MM-DD-slug.md)
├── _logo/                    # Source assets — NOT served by Jekyll
│   ├── process_logos.py      # White-bg → transparent PNG script
│   ├── social-preview.html   # Local OG image preview (open in browser)
│   └── README.md             # Asset table with previews and origins
├── assets/
│   ├── css/style.css         # All styles — CSS custom properties, no framework
│   ├── images/               # Optimised WebP + JPG/PNG served to visitors
│   │   └── press/            # Preview images for the press materials post
│   ├── press/                # Full-resolution downloads (linked from press post)
│   └── kiez-wm-2026.ics     # Downloadable calendar invite
├── index.html                # Main page
├── CNAME                     # Custom domain for GitHub Pages
├── LICENSE                   # CC BY-NC 4.0
├── CLAUDE.md                 # AI/developer conventions for this repo
└── Gemfile                   # Jekyll + webrick
```

---

## Features

### Registration form (formsubmit.co)

No backend needed. The form posts to `https://formsubmit.co/<hash>`. On success it redirects to `/?danke=1`, which JS detects to show a thank-you modal, then cleans the URL with `history.replaceState`.

Fields: name (required), email (required), phone (`type="tel"`, optional), class dropdown (required), free-text message (optional), DSGVO consent checkbox (required).

**Fetching submissions** (max 5×/day, auto-deleted after 30 days):

```bash
# Step 1 — request API key (delivered to the form email address)
curl -X GET https://formsubmit.co/api/get-apikey/moabit-2026@pimpmycargo.bike

# Step 2 — fetch submissions
curl -X GET https://formsubmit.co/api/get-submissions/<apikey>
```

### Email obfuscation

The contact address never appears as plain text in HTML. It is stored base64-encoded in a `data-em` attribute and decoded at runtime by JS:

```html
<a href="#" class="obf-mail" data-em="bW9hYml0LTIwMjZAcGltcG15Y2FyZ28uYmlrZQ==">moabit-2026 [at] pimpmycargo.bike</a>
```

The decoder in `_layouts/default.html` handles all `.obf-mail` elements automatically.

### Floating walk-in badge

A fixed orange pill in the bottom-right corner reads "Anmeldung auch vor Ort möglich" and scrolls to `#anmeldung`. Implemented as `.badge-walkin` in `style.css` + an `<a>` tag in `index.html`.

### Jump navigation

A sticky nav below the hero links to all page sections (`#info`, `#klassen`, `#anmeldung`, `#faq`, `#neuigkeiten`). Styled with `.jump-nav` in `style.css`.

### Calendar download

`assets/kiez-wm-2026.ics` uses `TZID=Europe/Berlin` for correct local time. Listed in `_config.yml` under `include:` so Jekyll copies it to `_site/`.

### Social media preview (OG + Twitter Card)

`_layouts/default.html` emits `og:image` and `twitter:image` meta tags. By default all pages use `/assets/images/og-preview.jpg` (1200×630). Blog posts with their own hero image should override this via front matter:

```yaml
---
title: "Post title"
date: 2026-05-01
social_media_preview_image: /assets/images/og-my-post.jpg
---
```

Generate the 1200×630 crop with Python/Pillow (center-crop, scale to cover):

```python
from PIL import Image
src = Image.open("_logo/my-source.jpg").convert("RGB")
tw, th = 1200, 630
scale = max(tw / src.width, th / src.height)
nw, nh = round(src.width * scale), round(src.height * scale)
resized = src.resize((nw, nh), Image.LANCZOS)
left, top = (nw - tw) // 2, (nh - th) // 2
resized.crop((left, top, left + tw, top + th)).save("assets/images/og-my-post.jpg", "JPEG", quality=90, optimize=True)
```

**Previewing**: open `_logo/social-preview.html` in a browser (no server needed) to see how `og-preview.jpg` renders on Facebook, Twitter/X, and WhatsApp. Update this file whenever `og-preview.jpg` or the OG text changes.

### Image optimisation pipeline

All images are served as WebP with a JPG/PNG fallback via `<picture>` + `srcset`. Originals stay in `_logo/` and are never served directly.

**Blog post images** (full-width, max 780px CSS):

```python
from PIL import Image
src = Image.open("_logo/my-photo.jpg").convert("RGB")
for w in [780, 1560]:
    h = round(src.height * w / src.width)
    r = src.resize((w, h), Image.LANCZOS)
    r.save(f"assets/images/my-photo-{w}w.webp", "WEBP", quality=85)
    r.save(f"assets/images/my-photo-{w}w.jpg", "JPEG", quality=85)
```

```html
<picture>
  <source type="image/webp"
    srcset="/assets/images/my-photo-780w.webp 780w,
            /assets/images/my-photo-1560w.webp 1560w"
    sizes="min(92vw, 780px)">
  <img src="/assets/images/my-photo-780w.jpg"
       srcset="/assets/images/my-photo-780w.jpg 780w,
               /assets/images/my-photo-1560w.jpg 1560w"
       sizes="min(92vw, 780px)"
       alt="…" style="width:100%;height:auto;border-radius:12px;">
</picture>
```

**Portrait/icon images** (e.g. class silhouettes, max 320px CSS): use 320w/640w instead. Use PNG fallback to preserve transparency.

**CSS backgrounds**: use `image-set()` for WebP-first loading:

```css
background-image: image-set(url('img-480w.webp') 1x, url('img-960w.webp') 2x);
```

### Logo silhouette processing

`_logo/process_logos.py` converts white-background PNGs to pure black transparent PNGs:
- Pixels with luminance < 50% **and** existing alpha ≥ 50% → pure black, fully opaque
- Everything else → fully transparent

```bash
cd _logo
pip install Pillow numpy
python3 process_logos.py size_pro.png size_boomer.png size_oldies.png
```

### Press materials

`_posts/YYYY-MM-DD-pressematerial.md` lists all downloadable assets for journalists and social media. Structure:
- **Previews** in `assets/images/press/` — WebP + JPG/PNG at display size
- **Originals** in `assets/press/` — full-resolution, uncompressed, linked for download

---

## Adding a blog post

Create `_posts/YYYY-MM-DD-slug.md`:

```yaml
---
title: "Dein Titel"
date: 2026-05-01
social_media_preview_image: /assets/images/og-my-post.jpg   # optional
---

Inhalt hier …
```

The post appears automatically in the "Neuigkeiten" section on the home page. If the post has a hero image, generate a 1200×630 OG crop (see above) and set `social_media_preview_image`.

---

## Local development

Requires Ruby 3.1.2 (see `.ruby-version`; rbenv picks it up automatically).

```bash
bundle install
bundle exec jekyll serve
# → http://localhost:4000
```

---

## Deployment

Push to `main` → GitHub Pages builds and deploys automatically.

The `CNAME` file tells GitHub Pages to serve the site at the custom domain and provision the TLS certificate. Enable "Enforce HTTPS" in Settings → Pages once the certificate is issued.

---

## Credits

| Tool | Use |
|---|---|
| [Claude Code](https://claude.ai/code) | AI — site build, image processing |
| [Gemini](https://gemini.google.com) | AI — class icon generation |
| [Vinilo](https://apps.apple.com/de/app/vinilo-crafting/id1554518531) | Creative tool — additional assets |

---

## License

[Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/) — free to share and adapt, not for commercial use. Attribution required.
