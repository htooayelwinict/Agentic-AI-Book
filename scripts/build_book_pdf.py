#!/usr/bin/env python3
"""Build the v0.1 book PDF from Markdown chapters.

The renderer intentionally uses Chromium via Playwright instead of drawing text
with ReportLab. Browser layout gives much better Myanmar text shaping and image
handling for this manuscript.
"""

from __future__ import annotations

import argparse
import html
import os
import re
from pathlib import Path
from typing import Iterable

import markdown
from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CHAPTERS = ROOT / "book" / "chapters"
DEFAULT_OUTPUT = ROOT / "output" / "pdf" / "agentic-ai-free-guide-v0.1.pdf"
DEFAULT_HTML = ROOT / "output" / "pdf" / "agentic-ai-free-guide-v0.1.html"
DEFAULT_CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")

URL_RE = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|#)", re.IGNORECASE)
MD_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HTML_IMAGE_RE = re.compile(r'(<img\b[^>]*\bsrc=["\'])([^"\']+)(["\'])', re.IGNORECASE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build Agentic AI book PDF")
    parser.add_argument("--chapters", type=Path, default=DEFAULT_CHAPTERS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--html", type=Path, default=DEFAULT_HTML)
    parser.add_argument("--chrome", type=Path, default=DEFAULT_CHROME)
    parser.add_argument("--keep-html", action="store_true", help="Keep generated HTML next to the PDF")
    return parser.parse_args()


def chapter_files(chapters_dir: Path) -> list[Path]:
    files = sorted(chapters_dir.glob("*.md"))
    if not files:
        raise SystemExit(f"No chapter markdown files found in {chapters_dir}")
    return files


def read_title(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return path.stem


def to_file_uri(path: Path) -> str:
    return path.resolve().as_uri()


def resolve_src(src: str, base_dir: Path, missing: list[Path]) -> str:
    if URL_RE.match(src):
        return src
    resolved = (base_dir / src).resolve()
    if not resolved.exists():
        missing.append(resolved)
    return to_file_uri(resolved)


def rewrite_image_paths(markdown_text: str, base_dir: Path, missing: list[Path]) -> str:
    def md_repl(match: re.Match[str]) -> str:
        alt = match.group(1)
        src = match.group(2)
        return f"![{alt}]({resolve_src(src, base_dir, missing)})"

    text = MD_IMAGE_RE.sub(md_repl, markdown_text)

    def html_repl(match: re.Match[str]) -> str:
        return f"{match.group(1)}{resolve_src(match.group(2), base_dir, missing)}{match.group(3)}"

    return HTML_IMAGE_RE.sub(html_repl, text)


def md_to_html(markdown_text: str) -> str:
    converted = markdown.markdown(
        markdown_text,
        extensions=[
            "markdown.extensions.extra",
            "markdown.extensions.sane_lists",
            "markdown.extensions.toc",
        ],
        output_format="html5",
    )
    return re.sub(r'<a\s+href="[^"]*"[^>]*>(.*?)</a>', r'<span class="link">\1</span>', converted)


def build_toc(files: Iterable[Path]) -> str:
    items = []
    for index, path in enumerate(files, start=1):
        title = html.escape(read_title(path))
        items.append(f'<li><span class="link">{title}</span></li>')
    return "<ol>" + "\n".join(items) + "</ol>"


def build_html(files: list[Path]) -> tuple[str, list[Path]]:
    missing_images: list[Path] = []
    sections = []
    for index, path in enumerate(files, start=1):
        raw = path.read_text(encoding="utf-8")
        raw = rewrite_image_paths(raw, path.parent, missing_images)
        body = md_to_html(raw)
        title = html.escape(read_title(path))
        section_class = "chapter frontmatter" if index <= 3 else "chapter"
        sections.append(
            f'<div class="page-break"></div>\n<section class="{section_class}" id="chapter-{index}" data-title="{title}">\n{body}\n</section>'
        )

    styles = """
    @page {
      size: A4;
      margin: 22mm 18mm 46mm 18mm;
    }

    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      color: #171717;
      background: #ffffff;
      font-family: "Noto Sans Myanmar", "Myanmar MN", "Myanmar Sangam MN", "Noto Serif Myanmar", serif;
      font-size: 11.2pt;
      line-height: 1.82;
      letter-spacing: 0;
    }

    .cover {
      height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      page-break-after: always;
      break-after: page;
      overflow: hidden;
    }

    .cover h1 {
      margin: 0 0 18px;
      font-size: 31pt;
      line-height: 1.35;
      font-weight: 800;
    }

    .cover .subtitle {
      max-width: 680px;
      color: #44403c;
      font-size: 14pt;
      line-height: 1.7;
    }

    .cover .meta {
      margin-top: 42px;
      color: #57534e;
      font-size: 10pt;
      line-height: 1.7;
    }

    .toc {
      height: 100vh;
      overflow: hidden;
      position: relative;
    }

    .toc::after,
    .frontmatter::after {
      content: "";
      position: absolute;
      left: 0;
      right: 0;
      bottom: 0;
      height: 36mm;
      background: #ffffff;
    }

    .page-break {
      break-before: page;
      page-break-before: always;
      height: 0;
      overflow: hidden;
    }

    .toc h1 {
      font-size: 20pt;
    }

    .toc ol {
      padding-left: 26px;
    }

    .toc li {
      margin: 5px 0;
      line-height: 1.55;
    }

    .chapter {
      page-break-before: auto;
      break-before: auto;
    }

    .frontmatter {
      position: relative;
      min-height: 82vh;
    }

    .chapter:first-of-type {
      page-break-before: auto;
    }

    h1, h2, h3, h4 {
      color: #111827;
      line-height: 1.45;
      page-break-after: avoid;
      break-after: avoid;
      font-weight: 800;
    }

    h1 {
      margin: 0 0 22px;
      font-size: 21pt;
    }

    h2 {
      margin: 28px 0 12px;
      font-size: 16pt;
    }

    h3 {
      margin: 24px 0 10px;
      font-size: 13.5pt;
    }

    p {
      margin: 0 0 11px;
      text-align: left;
      text-wrap: pretty;
      orphans: 3;
      widows: 3;
    }

    a {
      color: #1d4ed8;
      text-decoration: none;
      overflow-wrap: anywhere;
    }

    .link {
      color: #1d4ed8;
      overflow-wrap: anywhere;
    }

    blockquote {
      margin: 16px 0 18px;
      padding: 12px 15px;
      border-left: 4px solid #2563eb;
      background: #f8fafc;
      color: #1f2937;
      page-break-inside: avoid;
      break-inside: avoid;
    }

    ul, ol {
      margin: 0 0 13px 22px;
      padding: 0;
    }

    li {
      margin: 4px 0;
      padding-left: 2px;
    }

    code {
      font-family: "SFMono-Regular", Menlo, Consolas, monospace;
      font-size: 0.88em;
      background: #f3f4f6;
      border-radius: 4px;
      padding: 0.08em 0.28em;
    }

    pre {
      margin: 14px 0 16px;
      padding: 12px 14px;
      background: #111827;
      color: #f9fafb;
      border-radius: 8px;
      overflow-wrap: anywhere;
      white-space: pre-wrap;
      page-break-inside: avoid;
      break-inside: avoid;
    }

    pre code {
      color: inherit;
      background: transparent;
      padding: 0;
      font-size: 8.7pt;
      line-height: 1.58;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      margin: 16px 0;
      font-size: 9.2pt;
      page-break-inside: avoid;
      break-inside: avoid;
    }

    th, td {
      border: 1px solid #d4d4d8;
      padding: 7px 8px;
      vertical-align: top;
    }

    th {
      background: #f4f4f5;
      font-weight: 700;
    }

    img {
      display: block;
      max-width: 100%;
      height: auto;
      margin: 14px auto 8px;
      border: 1px solid #d4d4d8;
      border-radius: 6px;
      page-break-inside: avoid;
      break-inside: avoid;
    }

    hr {
      border: 0;
      border-top: 1px solid #d6d3d1;
      margin: 24px 0;
    }

    .sourceCode,
    figure,
    blockquote,
    table {
      page-break-inside: avoid;
      break-inside: avoid;
    }
    """

    return f"""<!doctype html>
<html lang="my">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Agentic AI အခမဲ့လမ်းညွှန်</title>
  <style>{styles}</style>
</head>
<body>
  <section class="cover">
    <h1>Agentic AI အခမဲ့လမ်းညွှန်</h1>
    <div class="subtitle">မြန်မာ Developer များအတွက် Agent, Tool, MCP, RAG, Coding Agent နှင့် DevOps Automation လက်တွေ့အခြေခံစာအုပ်</div>
    <div class="meta">
      Htoo Aye Lwin<br>
      v0.1 public review build<br>
      CC BY-NC-SA 4.0
    </div>
  </section>
  <div class="page-break"></div>
  <section class="toc">
    <h1>မာတိကာ</h1>
    {build_toc(files)}
  </section>
  {"".join(sections)}
</body>
</html>
""", missing_images


def render_pdf(html_path: Path, output_path: Path, chrome_path: Path) -> None:
    header_template = "<div></div>"
    footer_template = """
    <div style="width:100%; font-size:8px; color:#737373; padding:0 18mm; display:flex; justify-content:space-between; font-family: Arial, sans-serif;">
      <span>Agentic AI Guide</span>
      <span><span class="pageNumber"></span> / <span class="totalPages"></span></span>
    </div>
    """

    with sync_playwright() as p:
        launch_kwargs = {"headless": True}
        if chrome_path.exists():
            launch_kwargs["executable_path"] = str(chrome_path)
        browser = p.chromium.launch(**launch_kwargs)
        try:
            page = browser.new_page(viewport={"width": 1240, "height": 1754}, device_scale_factor=1)
            page.emulate_media(media="print")
            page.goto(html_path.resolve().as_uri(), wait_until="networkidle")
            page.pdf(
                path=str(output_path),
                format="A4",
                print_background=True,
                display_header_footer=True,
                header_template=header_template,
                footer_template=footer_template,
                margin={"top": "18mm", "right": "16mm", "bottom": "44mm", "left": "16mm"},
                prefer_css_page_size=True,
            )
        finally:
            browser.close()


def main() -> None:
    args = parse_args()
    files = chapter_files(args.chapters)
    html_text, missing_images = build_html(files)
    if missing_images:
        formatted = "\n".join(f"- {path}" for path in missing_images)
        raise SystemExit(f"Missing image assets:\n{formatted}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.html.parent.mkdir(parents=True, exist_ok=True)
    args.html.write_text(html_text, encoding="utf-8")
    render_pdf(args.html, args.output, args.chrome)

    print(f"Wrote PDF: {args.output}")
    print(f"Wrote HTML: {args.html}")
    if not args.keep_html:
        # Keep the HTML by default during RC work; the flag name is retained for
        # compatibility with future cleanup automation.
        pass


if __name__ == "__main__":
    main()
