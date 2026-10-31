"""Sanity checks for the portfolio. Run with:  pytest tests/"""
import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = (ROOT / "index.html").read_text(encoding="utf-8")
SECTION_IDS = ["hero", "gate", "pathways", "lessons", "honours", "credentials", "eternity"]


def strip_comments(html):
    return re.sub(r"<!--.*?-->", "", html, flags=re.S)


def test_html_pages_parse():
    for name in ("index.html", "404.html"):
        HTMLParser().feed((ROOT / name).read_text(encoding="utf-8"))


def test_local_asset_references_exist():
    html = strip_comments(INDEX)
    refs = set(re.findall(r'(?:src|href)="((?!https?:|mailto:|data:|#|/)[^"]+)"', html))
    missing = sorted(r for r in refs if not (ROOT / r).exists())
    assert not missing, f"missing local assets: {missing}"


def test_every_section_exists_and_is_linked():
    for sid in SECTION_IDS:
        assert f'id="{sid}"' in INDEX, f"missing section #{sid}"
    for sid in SECTION_IDS[1:]:
        assert f'href="#{sid}"' in INDEX, f"nothing links to #{sid}"


def test_anchor_targets_resolve():
    ids = set(re.findall(r'id="([^"]+)"', INDEX))
    targets = set(re.findall(r'href="#([^"]+)"', strip_comments(INDEX)))
    assert not (targets - ids), f"anchors with no target: {sorted(targets - ids)}"


def test_seo_metadata_present():
    for needle in ('<title>', 'name="description"', 'rel="canonical"', 'property="og:image"', 'name="twitter:card"'):
        assert needle in INDEX, f"missing {needle}"


def test_json_ld_is_valid_person():
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', INDEX, flags=re.S)
    assert m, "no JSON-LD block"
    data = json.loads(m.group(1))
    assert data["@type"] == "Person" and data["name"] == "Gaurav Rajbhar"


def test_no_remote_scripts_or_fonts():
    html = strip_comments(INDEX)
    assert not re.search(r'<script[^>]+src="https?://', html), "remote script found"
    assert not re.search(r'fonts\.(googleapis|gstatic)\.com', html), "remote font found"


def test_external_links_are_safe():
    html = strip_comments(INDEX)
    for tag in re.findall(r'<a [^>]*target="_blank"[^>]*>', html):
        assert "noopener" in tag, f"target=_blank without rel=noopener: {tag[:80]}"


def test_manifest_and_sitemap():
    manifest = json.loads((ROOT / "site.webmanifest").read_text(encoding="utf-8"))
    for icon in manifest["icons"]:
        assert (ROOT / icon["src"]).exists(), icon["src"]
    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    assert "https://rezzup.github.io/Yokoso/" in sitemap


def jpeg_size(path):
    """Read width and height from a JPEG's SOF marker (no Pillow needed)."""
    data = path.read_bytes()
    i = 2
    while i < len(data):
        assert data[i] == 0xFF, "bad JPEG marker"
        marker, length = data[i + 1], int.from_bytes(data[i + 2:i + 4], "big")
        if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
            return int.from_bytes(data[i + 7:i + 9], "big"), int.from_bytes(data[i + 5:i + 7], "big")
        i += 2 + length
    raise AssertionError("no SOF marker found")


def test_social_image_is_jpeg_1200x630_and_referenced():
    img = ROOT / "assets" / "og-image.jpg"
    assert jpeg_size(img) == (1200, 630)
    assert "assets/og-image.jpg" in INDEX
    assert INDEX.count("assets/og-image.jpg") >= 2, "both og:image and twitter:image should use it"


def test_noscript_fallback_shows_content():
    m = re.search(r"<noscript><style>(.*?)</style></noscript>", INDEX, flags=re.S)
    assert m, "missing <noscript> fallback"
    assert "[data-rv]" in m.group(1) and "#pre" in m.group(1)


def test_more_work_links_have_accessible_names():
    block = INDEX[INDEX.index('class="more"'):INDEX.index("</ul>", INDEX.index('class="more"'))]
    links = re.findall(r"<a [^>]*>", block)
    assert links, "no links found in the More work block"
    for tag in links:
        assert "aria-label=" in tag, f"link without aria-label: {tag[:90]}"


def test_no_leftover_escape_junk_in_text_files():
    """Catches files that were generated with literal '\\n' sequences instead of newlines."""
    for p in list(ROOT.glob("*.md")) + list((ROOT / "docs").glob("*.md")) + list((ROOT / "tests").glob("*.py")):
        text = p.read_text(encoding="utf-8")
        assert text.count("\\n") < 3 or "\n" in text.strip("\n"), f"suspicious literal \\n in {p.name}"
