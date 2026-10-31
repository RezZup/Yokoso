<div align="center">

![Gaurav Rajbhar — Portfolio](assets/portfolio-preview.webp)

# Yokoso — Gaurav Rajbhar's Portfolio

**A cinematic, scroll-driven WebGL portfolio — a night walk through a Kyoto mountain temple.**

Software Engineer · Full Stack · AI/ML

[![License: MIT](https://img.shields.io/badge/license-MIT-c9a24a)](LICENSE)
[![Deploy: GitHub Pages](https://img.shields.io/badge/deploy-GitHub%20Pages-e0231c)](#-deployment)
[![Last commit](https://img.shields.io/github/last-commit/RezZup/Yokoso)](https://github.com/RezZup/Yokoso/commits/main)
[![quality](https://github.com/RezZup/Yokoso/actions/workflows/quality.yml/badge.svg)](https://github.com/RezZup/Yokoso/actions/workflows/quality.yml)

[**Live site →**](https://rezzup.github.io/Yokoso/) &nbsp;·&nbsp; [GitHub](https://github.com/RezZup) &nbsp;·&nbsp; [LinkedIn](https://www.linkedin.com/in/gauravrajbhar00) &nbsp;·&nbsp; [Résumé](https://drive.google.com/file/d/1AzFnQRpkQEt-5lDo_UKrimBbRCY4qtZL/view?usp=sharing) &nbsp;·&nbsp; [Email](mailto:Gauravrajbhar2115@gmail.com)

</div>

---

## ✨ What this is

A single-page portfolio built as a night walk through a Kyoto mountain temple. The environment is a fixed, full-viewport Three.js scene; scrolling drives one continuous camera path, so every section arrives as a newly composed shot rather than a page jump.

The page has six chapters plus a footer:

| # | Chapter | What's in it |
|---|---|---|
| 01 | About | Who I am, portrait, quick stats |
| 02 | Selected Projects | Three featured projects with live 3D mini-viewports, plus a list of more work with live demos |
| 03 | Skills | Languages, AI/ML, backend, full stack, data & DevOps |
| 04 | Achievements | OpenAI × NxtWave Buildathon, hackathons, DSA practice |
| 05 | Credentials | B.Tech CSE at LPU and certifications |
| 06 | Contact | Email, résumé, GitHub, LinkedIn |

## 🧑‍💻 Featured projects

| Project | What it is | Stack | Repo |
|---|---|---|---|
| **ClothyRec** | Visual fashion recommender: clothing images become embeddings and visually similar items are retrieved | Python · PyTorch · ConvNeXt Tiny · OpenCLIP · FAISS | [Clothy-.-Rec](https://github.com/RezZup/Clothy-.-Rec) |
| **Suraksha Setu** | Disaster-information platform with multilingual interfaces and retrieval-based answers. State winner and national finalist, OpenAI × NxtWave Buildathon | AI/ML · RAG · Multilingual · Weather data | [Suraksha-Setu](https://github.com/RezZup/Suraksha-Setu) |
| **AlumUnity** | Alumni networking platform: mentorship, networking, real-time communication | React · shadcn/ui · Node.js · Express · MongoDB | [AlmuminiV3](https://github.com/RezZup/AlmuminiV3) |

More work, including live demos, is listed in [`LINKS.md`](LINKS.md) and in [`ALL_PROJECTS_MASTER_DIRECTORY.md`](ALL_PROJECTS_MASTER_DIRECTORY.md).

## 🎬 Features

- **Procedural 3D world** — worship hall, torii gate, a 26-riser stone flight, lanterns, maples, rocks, wooded ridge, haze, embers, rain, water ripples with a planar mirror, a leaf fall and a vermilion moon, all built in code (no model files)
- **Scroll-driven camera** — an 8-waypoint Catmull-Rom path, smoothed with Lenis ([details](docs/BEZIER_CAMERA_ARCHITECTURE.md))
- **Live mini-viewports** — each featured project card is a live window onto the same scene from its own camera angle, and it pushes in when you hover
- **Cinematic finish** — word-by-word reveals, parallax foreground cutouts, film grain, vignette and bloom
- **Adaptive quality** — pixel ratio is capped and the renderer trades resolution for frame rate on its own; a low-quality profile is picked automatically on touch devices
- **Accessible by default** — reduced-motion support, semantic landmarks, keyboard skip link, labelled links
- **Degrades gracefully** — a plain readable page with JavaScript off (`<noscript>` styles) or when WebGL can't start (built-in fallback)
- **Zero build tooling** — one HTML file, local assets, relative paths; deploys anywhere static
- **No trackers, no frameworks, no remote fonts** — fonts are embedded in `fonts.css`

## 🗂 Project structure

```
├── index.html                  # the entire site (markup + styles + scene code)
├── 404.html                    # themed not-found page (GitHub Pages)
├── assets/                     # og-image.jpg (link previews), README banner, favicon, app icons
├── secret-pathways-assets/
│   ├── three.min.js            # Three.js runtime (local)
│   ├── lenis.min.js, lenis.css # Lenis smooth scrolling (local)
│   ├── fonts.css               # fonts embedded as base64 (Onest, Noto JP, wordmark)
│   ├── foreground/png/         # WebP cutout layers (sakura, pines, lanterns…)
│   ├── generated/              # cinematic stills
│   └── portrait/               # About-section portrait
├── docs/                       # architecture notes (see below)
├── src/shaders/                # standalone GLSL reference snippets (not loaded by the site)
├── tests/test_site.py          # sanity checks run in CI
├── .github/workflows/          # quality.yml: HTML, assets, links, tests
├── LINKS.md                    # résumé, repositories, live demos, profiles
├── ALL_PROJECTS_MASTER_DIRECTORY.md  # long-form write-ups of every project
├── PROMPT.md                   # original design specification
├── robots.txt · sitemap.xml · site.webmanifest   # SEO and PWA metadata
└── LICENSE                     # MIT
```

## 🚀 Run locally

Any static server works — there is no build step:

```bash
git clone https://github.com/RezZup/Yokoso.git
cd Yokoso
python3 -m http.server 8000
# open http://localhost:8000
```

### Quality switches

The scene reads a few URL parameters, handy for debugging on slow hardware:

| Parameter | Effect |
|---|---|
| `?q=low` / `?q=high` | Force the low or high quality profile |
| `?dpr=1` | Cap the pixel ratio |
| `?post=0` | Turn off the post-processing chain (bloom etc.) |
| `?shadow=0` | Turn off shadows |
| `?adapt=0` | Lock the resolution scale instead of adapting it |

## ✅ Checks

```bash
pip install pytest
pytest tests/
```

CI (`.github/workflows/quality.yml`) parses `index.html` and `404.html`, verifies that every local asset reference resolves, runs the tests above and checks links.

## 🌐 Deployment

Deployed with **GitHub Pages**:

1. Repo → **Settings → Pages**
2. Source: *Deploy from a branch* → Branch: `main`, folder: `/ (root)`
3. The site goes live at <https://rezzup.github.io/Yokoso/>

## 📝 Customizing

- **Résumé button** — links to Google Drive. To serve a local PDF instead, add it at `assets/Gaurav-Rajbhar-Resume.pdf` and update the `href` in the Contact section of `index.html`
- **Project previews** — the project cards accept preview imagery inside each `card-fr` frame
- **Social preview image** — link previews use `assets/og-image.jpg` (1200 × 630, JPEG, because LinkedIn and X handle JPEG more reliably than WebP). Replace it, keeping the size and filename. `assets/portfolio-preview.webp` is only the README banner

## 📚 Docs

- [Technical specifications](docs/TECHNICAL_SPECIFICATIONS.md)
- [Camera architecture](docs/BEZIER_CAMERA_ARCHITECTURE.md)
- [Procedural 3D world guide](docs/PROCEDURAL_3D_WORLD_GUIDE.md)
- [Performance notes and budget](docs/WEBGL_PERFORMANCE_AUDIT.md)

## 🙏 Credits

- Smooth scrolling: [Lenis](https://github.com/darkroomengineering/lenis)
- Rendering: [Three.js](https://threejs.org/)

## 📄 License

[MIT](LICENSE) © 2026 Gaurav Rajbhar
