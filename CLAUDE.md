# CLAUDE.md — Moabiter Lastenlaufrad Kiez-WM 2026

## Build & run

```bash
bundle exec jekyll build       # one-off build → _site/
bundle exec jekyll serve       # local dev at http://localhost:4000
```

Requires Ruby 3.1.2 (set in `.ruby-version`; rbenv picks it up automatically).  
Never commit the `_site/` directory or `.DS_Store` files.

## Deploy

Push to `main` → GitHub Pages builds and deploys automatically.  
Live site: **https://moabit.pimpmycargo.bike**  
Remote: `git@github.com:falkorichter/moabit-lastenlaufrad-champion-2026.git`

After every change: commit the relevant source files and push. The user expects this to happen as part of completing a task unless told otherwise.

## Language

All user-facing text is in **German**. Keep it that way. Do not switch to English in copy, labels, placeholders, or error messages.

## Code conventions

- No CSS framework — all styles live in `assets/css/style.css` using CSS custom properties (`--teal`, `--orange`, etc.)
- No JS framework — vanilla JS only, inline in `_layouts/default.html` before `</body>`
- No comments in CSS/JS/HTML unless the reason is non-obvious
- Do not add new layout files or partials unless strictly necessary — the site intentionally has minimal structure

## Email obfuscation

The contact email (`moabit-2026@pimpmycargo.bike`) must **never** appear as plain text in any HTML output. Always use the base64 + `atob()` pattern:

```html
<a href="#" class="obf-mail" data-em="bW9hYml0LTIwMjZAcGltcG15Y2FyZ28uYmlrZQ==">moabit-2026 [at] pimpmycargo.bike</a>
```

The JS decoder in `_layouts/default.html` handles all `.obf-mail` elements automatically.

## Form (formsubmit.co)

- Form action: `https://formsubmit.co/2c8b381f690bbe6bcf6b8c3687e6a5a8`
- On success redirects to `/?danke=1` → JS shows the success modal
- Submissions archive: `GET https://formsubmit.co/api/get-submissions/<apikey>` (max 5×/day, 30-day retention)
- To request a fresh API key: `curl -X GET https://formsubmit.co/api/get-apikey/moabit-2026@pimpmycargo.bike`

## Key facts

| | |
|---|---|
| Event | 9. Mai 2026, 16:00 Uhr |
| Location | Zazza Frühlingsfest, Moabit, Berlin |
| Classes | Kindergarten (Die Pros), Grundschule (Lauf-Boomer), Erwachsene (Oldies) |
| Race bike | Super Mighty Junior – Cargo-Laufrad (super-bicycles.com) |
| Participants bring | Own helmet; optionally cycling gloves — race bike is provided |
| Organiser | Falko Richter / PimpMyCargo.bike |
| Instagram | [@pimpmycargo.bike](https://www.instagram.com/pimpmycargo.bike/) |
| Zazza Instagram | [@zazza_moabit](https://www.instagram.com/zazza_moabit/) |

## UTM convention for Super Bicycles links

```
utm_source=moabit-kiez-wm
utm_medium=referral
utm_campaign=kiez-wm-2026
utm_content=<placement>   ← about-section | faq | ...
utm_term=lastenlaufrad
```

## Adding a blog post

Create `_posts/YYYY-MM-DD-slug.md` with:

```yaml
---
title: "Titel"
date: 2026-05-09
---
```

Posts appear automatically in the "Neuigkeiten" section on the home page.
