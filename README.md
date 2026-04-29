# Moabiter Lastenlaufrad Kiez-Weltmeisterschaft 2026

Website for the first Moabiter Lastenlaufrad Kiez-WM, hosted at **[moabit.pimpmycargo.bike](https://moabit.pimpmycargo.bike)**.

## Event details

| | |
|---|---|
| **Date** | 9. Mai 2026, 16:00 Uhr |
| **Location** | Zazza Frühlingsfest, Moabit, Berlin |
| **Instagram** | [@zazza_moabit](https://www.instagram.com/zazza_moabit/) |
| **Contact** | moabit-2026@pimpmycargo.bike |
| **Organiser** | Falko Richter / [PimpMyCargo](https://www.pimpmycargo.bike) — [@pimpmycargo.bike](https://www.instagram.com/pimpmycargo.bike/) |

### Classes

| Class | Nickname |
|---|---|
| Kindergarten | Die Pros |
| Grundschule | Lauf-Boomer |
| Erwachsene | Oldies |

Official race bike: [Super Mighty Junior – Cargo-Laufrad](https://super-bicycles.com/products/super-mighty-junior-cargo-laufrad) by Super Bicycles.

## Tech stack

- [Jekyll](https://jekyllrb.com/) 4.x static site generator
- Hosted on **GitHub Pages** with custom domain `moabit.pimpmycargo.bike`
- DNS: CNAME at [united-domains.de](https://www.united-domains.de/) → `falkorichter.github.io`
- Registration form via [formsubmit.co](https://formsubmit.co) (no backend required); redirects to `/?danke=1` on success
- Submissions archive available via the [formsubmit API](https://formsubmit.co/documentation) — free, max 5 requests/day, data retained for 30 days
- Post-submission success modal: JS detects `?danke=1`, shows popup, cleans URL with `history.replaceState`
- Calendar download: `assets/kiez-wm-2026.ics` (Europe/Berlin timezone, MESZ/CEST)
- Email obfuscation: base64 + JS decode (`atob`) at runtime to deter scrapers — no plain `@` in HTML source
- Phone field uses `type="tel"` for native numeric keyboard on mobile

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
│   ├── default.html          # Base layout with footer, email obfuscation + success modal JS
│   └── post.html             # Blog post layout
├── _posts/                   # Blog posts (YYYY-MM-DD-title.md)
├── assets/
│   ├── css/style.css         # All styles — no framework
│   ├── images/logo.png       # Kid's crayon Lastenrad drawing
│   └── kiez-wm-2026.ics     # Downloadable calendar invite
├── index.html                # Main page (hero, info band, classes, form, FAQ, blog, success modal)
├── CNAME                     # Custom domain for GitHub Pages
└── Gemfile                   # Jekyll + webrick
```

## Deployment

Push to the `main` branch — GitHub Pages builds and deploys automatically.

The `CNAME` file tells GitHub Pages to serve the site at `moabit.pimpmycargo.bike` and provision a TLS certificate. HTTPS can be enforced in the repository Settings → Pages once the certificate has been issued (usually a few minutes after the first push with the CNAME file).

## Adding a blog post

Create a file in `_posts/` following Jekyll's naming convention:

```
_posts/YYYY-MM-DD-slug.md
```

With this front matter:

```yaml
---
title: "Dein Titel"
date: 2026-05-01
---

Inhalt hier …
```

The post will appear automatically in the "Neuigkeiten" section on the home page.
