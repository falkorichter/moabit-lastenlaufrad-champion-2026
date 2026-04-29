# Moabiter Lastenlaufrad Kiez-Weltmeisterschaft 2026

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

Website for the first Moabiter Lastenlaufrad Kiez-WM, hosted at **[moabit.pimpmycargo.bike](https://moabit.pimpmycargo.bike)**.

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

## Tech stack

- [Jekyll](https://jekyllrb.com/) 4.x static site generator
- Hosted on **GitHub Pages** with custom domain `moabit.pimpmycargo.bike`
- DNS: CNAME at [united-domains.de](https://www.united-domains.de/) → `falkorichter.github.io`
- Registration form via [formsubmit.co](https://formsubmit.co) (no backend required); redirects to `/?danke=1` on success
- Submissions archive via the formsubmit API — free, max 5 requests/day, data auto-deleted after 30 days
- Post-submission success modal: JS detects `?danke=1`, shows popup, cleans URL with `history.replaceState`
- Calendar download: `assets/kiez-wm-2026.ics` (Europe/Berlin timezone, MESZ/CEST)
- Email obfuscation: base64 + JS `atob()` at runtime — no plain `@` in HTML source
- Phone field uses `type="tel"` for native numeric keyboard on mobile
- DSGVO consent checkbox (required) before form submission
- Sticky jump nav linking to all page sections
- Class cards with size silhouette PNGs as background watermarks
- Submit button uses the Super Junior SVG logo (inline, `filter: invert(1)`)

## Image processing

Logo silhouettes (`size_pro`, `size_boomer`, `size_oldies`) were processed with Python/Pillow:
- White background → transparent
- Luminance threshold at 50%: dark pixels → pure black, light pixels → transparent
- Originals preserved in `_logo/`; processed `_transparent.png` versions in `assets/images/`

## Local development

Requires Ruby 3.1.2 (see `.ruby-version`).

```bash
bundle install
bundle exec jekyll serve
# → http://localhost:4000
```

## Project structure

```
moabit-2026/
├── _config.yml               # Site config, title, description
├── _layouts/
│   ├── default.html          # Base layout: footer, imprint, email obfuscation + success modal JS
│   └── post.html             # Blog post layout
├── _posts/                   # Blog posts (YYYY-MM-DD-title.md)
├── _logo/                    # Source logo files (not served)
├── assets/
│   ├── css/style.css         # All styles — no framework
│   ├── images/               # logo.png, SVG, silhouette PNGs
│   └── kiez-wm-2026.ics     # Downloadable calendar invite
├── index.html                # Main page (hero, info band, jump nav, classes, form, FAQ, blog, modal)
├── CNAME                     # Custom domain for GitHub Pages
├── LICENSE                   # CC BY-NC 4.0
└── Gemfile                   # Jekyll + webrick
```

## Deployment

Push to `main` → GitHub Pages builds and deploys automatically.

The `CNAME` file tells GitHub Pages to serve the site at `moabit.pimpmycargo.bike` and provision the TLS certificate. Enable "Enforce HTTPS" in Settings → Pages once the certificate is issued.

## formsubmit.co API

To fetch all submissions (max 5×/day):

```bash
# Step 1 — request API key (sent to moabit-2026@pimpmycargo.bike)
curl -X GET https://formsubmit.co/api/get-apikey/moabit-2026@pimpmycargo.bike

# Step 2 — fetch submissions
curl -X GET https://formsubmit.co/api/get-submissions/<apikey>
```

## Adding a blog post

Create `_posts/YYYY-MM-DD-slug.md` with:

```yaml
---
title: "Dein Titel"
date: 2026-05-01
---

Inhalt hier …
```

The post appears automatically in the "Neuigkeiten" section on the home page.

## Credits

| Tool | Use |
|---|---|
| [Claude Code](https://claude.ai/code) | AI — site build, image processing |
| [Gemini](https://gemini.google.com) | AI — class icon generation |
| [Vinilo](https://apps.apple.com/de/app/vinilo-crafting/id1554518531) | Creative tool — additional assets |

## License

[Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/) — free to share and adapt, not for commercial use. Attribution required.
