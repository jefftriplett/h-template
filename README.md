# h-templates

Experimental project for generating HTML in Python using Pydantic.

By Jeff Triplett.

## Installation

```bash
pip install h-template
```

## Usage

```python
from h import div, p, a, ul, li, html, head, body, title

# Simple tag with text
greeting = div()["Hello, World!"]
print(greeting)
# <div>Hello, World!</div>

# Tag with attributes (use class_ for "class" since it's a Python keyword)
container = div(class_="container", id="main")["Content here"]
print(container)
# <div class="container" id="main">Content here</div>

# Nested tags
nav = ul()[
    li()[a(href="/")["Home"]],
    li()[a(href="/about")["About"]],
]
print(nav)
# <ul><li><a href="/">Home</a></li><li><a href="/about">About</a></li></ul>

# Full document
doc = html()[
    head()[title()["My Page"]],
    body()[
        div(class_="container")[
            p()["Welcome to my page!"]
        ]
    ]
]
print(doc)
```

### Page with Meta and OpenGraph Tags

```python
from h import doctype, html, head, title, meta, body, h1, p

page_title = "My Awesome Page"
page_description = "A brief description of my page for search engines and social sharing."

doc = doctype()[
    html(lang="en")[
        head()[
            title()[page_title],
            meta(charset="utf-8"),
            meta(name="viewport", content="width=device-width, initial-scale=1"),

            # SEO meta tags
            meta(name="description", content=page_description),

            # OpenGraph tags
            meta(property="og:title", content=page_title),
            meta(property="og:description", content=page_description),
            meta(property="og:type", content="website"),
            meta(property="og:url", content="https://example.com/my-page"),
        ],
        body()[
            h1()[page_title],
            p()[page_description],
        ]
    ]
]
print(doc)
```

## Inspiration

- [Hyperscript](https://github.com/hyperhype/hyperscript)
- [hyperpython](https://github.com/ejplatform/hyperpython)

## Original Project

This project is based on [h](https://github.com/adamchainz/h) by Adam Johnson, licensed under the ISC License.
