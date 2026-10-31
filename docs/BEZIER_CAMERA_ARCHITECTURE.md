# Scroll-Driven Camera Architecture

Yokoso turns page scroll into a single continuous camera move through the scene. The path is a Catmull-Rom spline (`THREE.CatmullRomCurve3`) through eight hand-composed waypoints, one per `data-cam` section of the page.

## 1. Waypoints

Each waypoint stores a camera position `p`, a look-at target `t` and a field of view. The values below are taken from the `CAM` array in `index.html` (section 8, "the camera rig").

| # | Section | Camera position | Look-at target | FOV |
|---|---|---|---|---|
| 0 | Hero | 0.0, 4.05, 13.6 | 0.0, 6.60, −18.0 | 36 |
| 1 | About (the sanmon gate) | −5.6, 2.35, 11.6 | 1.2, 5.60, −14.0 | 48 |
| 2 | Projects (gardens) | 1.2, 3.60, 2.2 | −0.6, 7.50, −22.0 | 40 |
| 3 | Skills (craft) | 5.2, 2.10, −3.4 | −2.6, 7.00, −20.0 | 46 |
| 4 | Achievements | 2.6, 3.60, −7.4 | −1.4, 8.80, −26.0 | 45 |
| 5 | Credentials | 1.0, 5.20, −11.6 | −0.4, 11.0, −33.0 | 44 |
| 6 | Contact | 0.0, 7.60, −16.0 | 0.0, 13.0, −40.0 | 42 |
| 7 | Footer | 0.0, 10.5, −20.0 | 0.0, 3.00, −34.0 | 46 |

Two curves are built from these points, one for position and one for the target, both with tension `0.42`.

## 2. From scroll to progress

- Every element carrying `data-cam` is a section anchor. `measure()` records the scroll offset at which each section is centred in the viewport.
- `progressFor(y)` converts the current scroll offset into a fractional section index (for example `2.4` is 40% of the way from section 2 to section 3).
- The camera samples both curves at `progress / (waypoints − 1)`.
- Lenis provides the smoothed scroll value, and the rig adds its own smoothing (`RIG.smooth`) on top, so wheel, trackpad and touch input all produce the same easing.

## 3. Aspect-ratio handling

Every waypoint is composed for a wide frame. On a tall viewport (phones) the same numbers would crop the gate, so `fitAspect()` steps the camera back along its own view axis, lifts it slightly and widens the field of view. The correction fades in as the aspect ratio drops below roughly 1.62.

## 4. Pointer parallax and focus

The rig also holds pointer offsets (`RIG.mx`, `RIG.my`) for a small parallax drift, and a damped `focus` value (`RIG.focus` / `RIG.focusAmt`) that the page-wiring code sets.

## 5. Tuning

To change a shot, edit its entry in `CAM` and reload. Keep neighbouring waypoints close in direction: a large jump between two waypoints makes the spline overshoot.
