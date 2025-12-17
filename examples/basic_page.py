"""
Basic example: Generate a complete HTML page without any web framework.

Run with: python examples/basic_page.py
"""

from h import (
    doctype,
    html,
    head,
    title,
    meta,
    style,
    body,
    header,
    nav,
    main,
    footer,
    h1,
    h2,
    p,
    a,
    ul,
    li,
    div,
    span,
    img,
    comment,
)


def navbar(links: list[tuple[str, str]]) -> nav:
    """Create a navigation bar from a list of (text, url) tuples."""
    return nav(class_="navbar")[
        ul[[li[a(href=url)[text]] for text, url in links]]
    ]


def card(heading: str, content: str, image_url: str | None = None) -> div:
    """Create a card component."""
    children = []
    if image_url:
        children.append(img(src=image_url, alt=heading, class_="card-image"))
    children.append(h2[heading])
    children.append(p[content])
    return div(class_="card")[children]


def page(title_text: str, content) -> doctype:
    """Create a complete HTML page."""
    return doctype()[
        html(lang="en")[
            head[
                meta(charset="utf-8"),
                meta(name="viewport", content="width=device-width, initial-scale=1"),
                title[title_text],
                style[
                    """
                    body { font-family: system-ui, sans-serif; margin: 0; padding: 20px; }
                    .navbar ul { display: flex; gap: 1rem; list-style: none; padding: 0; }
                    .card { border: 1px solid #ddd; padding: 1rem; margin: 1rem 0; border-radius: 8px; }
                    footer { margin-top: 2rem; color: #666; }
                    """
                ],
            ],
            body[content],
        ]
    ]


def main_content():
    """Build the main page content."""
    return [
        comment("Header section"),
        header[
            h1["Welcome to h-templates"],
            p["A hyperscript-style HTML generation library for Python."],
        ],
        navbar([
            ("Home", "/"),
            ("About", "/about"),
            ("Contact", "/contact"),
        ]),
        comment("Main content"),
        main[
            card(
                "Getting Started",
                "Use Python to generate HTML with a clean, composable API.",
            ),
            card(
                "No Templates Needed",
                "Write your views entirely in Python - no template language to learn.",
            ),
            div[
                p["Features:"],
                ul[
                    li["Hyperscript-style syntax: ", span(class_="code")["div['content']"]],
                    li["Automatic HTML escaping for security"],
                    li["Void tags handled correctly (br, img, etc.)"],
                    li["Supports attributes, classes, and inline styles"],
                ],
            ],
        ],
        comment("Footer"),
        footer[
            p["Built with h-templates"],
            p["Python ", span[f"{__import__('sys').version_info.major}.{__import__('sys').version_info.minor}"]],
        ],
    ]


if __name__ == "__main__":
    html_output = str(page("h-templates Example", main_content()))
    print(html_output)

    # Optionally write to file
    with open("output.html", "w") as f:
        f.write(html_output)
    print("\nWritten to output.html")
