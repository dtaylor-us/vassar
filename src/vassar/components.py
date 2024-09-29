from fasthtml.components import (
    Nav,
    A,
    Link,
    Head,
    Footer,
    Small,
    Div,
)

def page_header():
    return Head(
        Link(
            rel="stylesheet",
            href="https://cdnjs.cloudflare.com/ajax/libs/tachyons/4.11.1/tachyons.min.css",
            type="text/css",
        ),
        Link(
            rel="stylesheet",
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css",
        )
    )

def page_nav():
    return Nav(
        Div(
            A("The Vassar Community Project", href="/", cls="link dim white b f6 f5-ns dib mr5 common-font"),
            cls="flex-grow-1"
        ),
        Div(
            A("History", href="/history", cls="link dim light-gray f6 f5-ns dib mr3 common-font"),
            A("Genealogical Map", href="/", cls="link dim light-gray f6 f5-ns dib mr3 common-font"),
            A("Vassar Sisters", href="/", cls="link dim light-gray f6 f5-ns dib mr3 common-font"),
            cls="flex"
        ),
        cls="flex justify-between pa3 pa4-ns overflow-wrap"
    )

def page_footer():
    return Footer(
        Small("© 2024 Sankofa Dua Project, All Rights Reserved", cls="f6 db tc common-font"),
        Div(
            A("Privacy Policy", href="/", cls="f6 dib ph2 link mid-gray dim common-font"),
            A("Terms of Use", href="/", cls="f6 dib ph2 link mid-gray dim common-font"),
            A("Contact Us", href="/", cls="f6 dib ph2 link mid-gray dim common-font"),
            cls="flex justify-center mt3",
        ),
        cls="pv4 ph3 ph5-m ph6-l"
    )