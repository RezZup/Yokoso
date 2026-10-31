# Technical Specifications

## Overview

| | |
|---|---|
| Type | Static single-page site, no build step |
| Rendering | Three.js (local copy, `secret-pathways-assets/three.min.js`) |
| Scrolling | Lenis (local copy) |
| Languages | HTML, CSS, vanilla JavaScript (one inline script wrapped in an IIFE) |
| Hosting | GitHub Pages, `main` branch, repository root |
| Trackers / analytics | None |
| Remote fonts | None; Onest, Noto JP and the wordmark face are embedded in `fonts.css` |

## Page structure

The page is a sequence of sections, each carrying a `data-cam` index that maps it to a camera waypoint (see [camera architecture](BEZIER_CAMERA_ARCHITECTURE.md)).

| `data-cam` | Section | id |
|---|---|---|
| 0 | Hero | `hero` |
| 1 | 01 About | `gate` |
| 2 | 02 Selected Projects | `pathways` |
| 3 | 03 Skills | `lessons` |
| 4 | 04 Achievements | `honours` |
| 5 | 05 Credentials | `credentials` |
| 6 | 06 Contact | `eternity` |
| 7 | Footer | — |

## Script layout

The inline script in `index.html` is organised in numbered sections:

| # | Section |
|---|---|
| 0 | Basics: URL parameters, helpers, reduced-motion and touch detection |
| 4 | WebGL renderer setup and quality profile |
| 5 | The world (see [world guide](PROCEDURAL_3D_WORLD_GUIDE.md)) |
| 6 | Planar mirror |
| 7 | Post-processing |
| 8 | Camera rig |
| 9 | Scroll to chapter mapping |
| 10 | Wordmark layout |
| 11 | Page wiring |
| 12 | Project-card viewports |
| 13 | Main loop |
| 14 | Booting |

## Runtime options

URL parameters read by the script:

| Parameter | Default | Meaning |
|---|---|---|
| `q` | `high` (`low` on touch devices) | Quality profile |
| `dpr` | 1.8 (1.4 when low) | Pixel-ratio cap |
| `post` | `1` | `0` disables post-processing |
| `shadow` | `1` (`0` when low) | `0` disables shadows |
| `adapt` | `1` | `0` locks the resolution scale |

## Accessibility

- Semantic landmarks and a keyboard skip link.
- `prefers-reduced-motion` blocks that keep the full reading experience without the motion.
- A custom cursor is used only on fine-pointer devices.
- Decorative foreground images use empty `alt` text and `aria-hidden`.

## SEO and metadata

- Title, description, canonical URL, Open Graph and Twitter card tags in `<head>`.
- `schema.org` `Person` JSON-LD with name, title, image, email and profile links.
- `robots.txt`, `sitemap.xml`, `site.webmanifest`, favicon and Apple touch icon.
- `404.html` is a themed not-found page and is set to `noindex`.

## Quality checks

`.github/workflows/quality.yml` runs on every push and pull request to `main`:

1. Parse `index.html` and `404.html`.
2. Verify every local `src` and `href` in `index.html` exists.
3. Run `pytest tests/`.
4. Check links in all HTML and Markdown files with lychee.

See [performance notes](WEBGL_PERFORMANCE_AUDIT.md) for measured page weight and the performance budget.
