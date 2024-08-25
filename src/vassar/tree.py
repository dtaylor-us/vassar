from fasthtml.components import (
    Nav,
    A,
    Link,
    Head,
    Title,
    Script,
    Div,
    Main,
    Span,
    I,
    Ul,
    Li,
    Button,
    P,
    H2,
)
from fasthtml.fastapp import fast_app, serve
from rich.console import Console
from starlette.responses import FileResponse, JSONResponse

from vassar.database import async_query, get_async_driver

console = Console()

app, rt = fast_app(live=True, debug=True)

GRAPH_DATA_QUERY = """
MATCH(p:Person) Return p
"""

UNION_DATA_QUERY = """
MATCH (parent1:Person)-[:CHILD_OF]->(child:Person)<-[:CHILD_OF]-(parent2:Person)
RETURN parent1.person_id AS parent1_id, parent2.person_id AS parent2_id, child.person_id AS child_id
"""


@rt("/{fname:path}.{ext:static}")
async def get(fname: str, ext: str):
    return FileResponse(f"public/{fname}.{ext}")


def find_person_by_name(people, name):
    for person in people.values():
        if person['name'] == name:
            return person
    return None


def build_subtree(person_id, people, unions):
    person = people[person_id]

    # Find children for this person
    children = []
    for union in unions.values():
        if union['parent1_id'] == person_id or union['parent2_id'] == person_id:
            child_person_id = union['child_id']
            child_tree = build_subtree(child_person_id, people, unions)
            children.append(child_tree)

    if not children:
        # If no children, return the person node
        return {"name": person['name'], "gender": person['gender'], "type": "person"}

    # Find the other parent in the union
    parent_union = None
    for union in unions.values():
        if union['child_id'] == person_id:
            parent_union = union
            break

    if parent_union:
        parent1 = people[parent_union['parent1_id']]
        parent2 = people[parent_union['parent2_id']]
        return {
            "type": "union",
            "parents": [
                {"name": parent1['name'], "gender": parent1['gender'], "type": "person"},
                {"name": parent2['name'], "gender": parent2['gender'], "type": "person"}
            ],
            "children": children
        }
    else:
        return {"name": person['name'], "gender": person['gender'], "type": "person"}


def build_family_tree(data, relationships):
    people = {}
    unions = {}

    root_person_name = "John Doe"

    # Populate the people dictionary from the EagerResult records
    for record in data.records:
        person_data = record['p']  # Assuming 'p' is the alias for the person node in your Cypher query
        person_id = person_data['person_id']
        person = {
            "id": person_id,
            "name": person_data["name"],
            "gender": person_data["gender"],
            "birthdate": person_data["birthdate"].iso_format()  # Adjust as needed for date formatting
        }
        people[person_id] = person

    # Populate the unions dictionary from the relationships
    for record in relationships.records:
        parent1_id = record["parent1_id"]
        parent2_id = record["parent2_id"]
        child_id = record["child_id"]
        unions[child_id] = {
            "parent1_id": parent1_id,
            "parent2_id": parent2_id,
            "child_id": child_id
        }

    # Find the target person (root person)
    target_person = find_person_by_name(people, root_person_name)
    if not target_person:
        return {"error": "Root person not found"}

    # The root of the family tree
    family_tree = {
        "name": "Root Node",
        "type": "root",
        "children": [build_subtree(target_person['id'], people, unions)]
    }

    return family_tree


@rt("/tree")
async def get(request):
    async with get_async_driver() as driver:
        people = await async_query(driver, GRAPH_DATA_QUERY)
        relationships = await async_query(driver, UNION_DATA_QUERY)
        root = build_family_tree(people, relationships)
        console.print(root)
        return JSONResponse(root)


@rt("/")
def get():
    return (
        Title("Family Tree Visualization"),
        Head(
            Link(
                rel="stylesheet",
                href="https://cdnjs.cloudflare.com/ajax/libs/tachyons/4.11.1/tachyons.min.css",
                type="text/css",
            ),
            Link(
                rel="stylesheet",
                href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css",
            ),
        ),
        Nav(
            A(
                "Graph DB Fundamentals",
                href="/",
                cls="link dim white b f6 f5-ns dib mr3",
            ),
            A("Home", href="/", cls="link dim light-gray f6 f5-ns dib mr3"),
            cls="pa3 pa4-ns",
        ),
        Main(
            Div(
                Span(
                    I(cls="fas fa-question-circle light-purple mb3"),
                    P("Help", cls="ml2"),
                    cls="flex pointer info-icon",
                ),
                Div(
                    Div(
                        Span("close X", cls="close-btn mb2 f6 light-purple pointer"),
                        cls="flex justify-end items-center",
                    ),
                    Ul(
                        Li("Zoom: Mouse wheel / touchpad scroll"),
                        Li("Pan: Click and drag."),
                        cls="pl3",
                    ),
                    cls="info-banner bg-navy pa3 ba br-rounded b--light-silver br2 shadow-1 dn",
                ),
                cls="info-container fixed bottom-2 right-2",
            ),
            H2("Family Tree Visualization", cls="tc"),
            Button(
                "Expand All",
                id="expand-all",
                cls="f6 link dim br-rounded ph3 pv2 mb4 mt2 dib white bg-dark-blue",
            ),
            Button(
                "Collapse All",
                id="collapse-all",
                cls="dn f6 link dim br-rounded ph3 pv2 mb4 mt2  white bg-dark-blue",
            ),
            Div(id="family-tree"),
            cls="container",
        ),
        Script(src="https://d3js.org/d3.v6.min.js"),
        Script(src="/public/js/tree.js"),
    )


if __name__ == "__main__":
    serve(port=8001, reload=True)
