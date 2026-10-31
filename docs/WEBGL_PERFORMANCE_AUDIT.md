# Performance Notes & Budget

This page records what has actually been measured, what is only a target, and how to measure the rest yourself.

## Page weight (measured)

Measured by loading `index.html` in headless Chrome from a local static server (no compression, no cache), then waiting for the scene to start. The page made no external requests, logged no console errors and had no failed requests.

| Viewport | Requests | Transferred |
|---|---|---|
| Desktop, 1440 × 900 | 13 | ≈ 2.3 MB |
| Mobile, 390 × 844 | 9 | ≈ 1.5 MB |

Foreground images are lazy-loaded, so the total grows a little as you scroll. On GitHub Pages the text files (HTML, JS, CSS) are also gzip-compressed, which makes them considerably smaller than the sizes below.

Largest items on disk:

| File or folder | Size on disk |
|---|---|
| `secret-pathways-assets/foreground/` (WebP cutouts) | ≈ 1.9 MB |
| `secret-pathways-assets/generated/` (cinematic stills) | ≈ 0.7 MB |
| `secret-pathways-assets/three.min.js` | ≈ 0.6 MB |
| `index.html` (markup, styles, scene code) | ≈ 0.26 MB |
| `secret-pathways-assets/fonts.css` (fonts embedded as base64) | ≈ 0.12 MB |
| `secret-pathways-assets/lenis.min.js` | ≈ 0.02 MB |

## Frame rate and GPU cost (not yet measured)

Frame rate depends heavily on the GPU, so it has not been recorded here. Headless Chrome with software rendering is far too slow to say anything useful about it. To fill this in, measure on real hardware:

1. Open the live site in Chrome, then open DevTools → **Performance** and record a full scroll from top to bottom.
2. Note the average and 1%-low frame rate, plus `renderer.info.render.calls` and `.triangles` (run `renderer.info` in the console if you expose the renderer, or use a tool such as Spector.js to count draw calls).
3. Repeat with `?q=low` and on a phone.
4. Paste the results into a table here, with the device and browser version.

## Built-in performance controls

The scene is fill-bound (several large alpha-blended layers plus a bloom chain), so pixels are the main lever:

- The pixel ratio is capped (1.8 on desktop, 1.4 on touch devices).
- The renderer adapts its resolution scale at runtime to hold its frame rate (turn off with `?adapt=0`).
- Touch devices default to the low profile; force it with `?q=low`.
- Shadows can be turned off with `?shadow=0`, post-processing with `?post=0`.
- Many small meshes are merged, or drawn with `InstancedMesh`, to limit draw calls.

## Budget (targets, not results)

| Metric | Target |
|---|---|
| Frame rate | 60 FPS on a mid-range laptop GPU, adaptive resolution allowed |
| First load, desktop | under 3 MB |
| First load, mobile | under 2 MB |
| Console errors | none |
