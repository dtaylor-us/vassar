from fasthtml.common import *

app, rt = fast_app(live=True, debug=True)


@rt("/{fname:path}.{ext:static}")
async def get(fname: str, ext: str):
    return FileResponse(f"public/{fname}.{ext}")


@rt('/')
def get(): return (Title("Family Tree Visualization"),
                   Head(Link(rel="stylesheet",
                             href="https://cdnjs.cloudflare.com/ajax/libs/tachyons/4.11.1/tachyons.min.css",
                             type="text/css")),
                   Nav(A("Graph DB Fundamentals", href="/", cls="link dim white b f6 f5-ns dib mr3"),
                       A("Home", href="/", cls="link dim light-gray f6 f5-ns dib mr3"),
                       cls="pa3 pa4-ns"),
                   Main(H1('Hello, World'), cls="container"))
