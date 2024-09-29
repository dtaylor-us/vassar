from fasthtml.components import (
    Title,
    Main,
    Article,
    Div,
    H1,
    Blockquote,
    P,
    Cite,
    Section,
    A,
    I,
    Span,
    H3,
    H4, Header, H2,
)

from fasthtml.fastapp import fast_app, serve
from starlette.responses import FileResponse

from vassar.components import page_header, page_nav, page_footer
from vassar.history import history_routes

app, rt = fast_app(live=True, debug=True)

@rt("/{fname:path}.{ext:static}")
async def get(fname: str, ext: str):
    return FileResponse(f"public/{fname}.{ext}")

class Svg:
    pass

@rt("/")
def get():
    return (
        Title("The Vassar Community Project"),
        page_header(),
        page_nav(),
        home_page(),
        page_footer(),
    )

def home_page():
    return Main(
        Article(
            Div(
                Div(
                    H1("The Vassar Community Project", cls="f1 f-headline-l fw1 i white-60"),
                    Blockquote(
                        P(
                            "In knowing our past, we find the strength to shape our future.",
                            cls="fw1 white-70"
                        ),
                        Cite(
                            "— Embracing the spirit of Sankofa: We look back to honor our roots and move forward with purpose.",
                            cls="f6 ttu fs-normal"),
                        cls="ph0 mh0 measure f4 lh-copy center"
                    ),
                    cls="dtc v-mid"
                ),
                cls="vh-100 dt w-100 tc bg-dark-gray white cover",
                style="background:url(http://mrmrs.github.io/photos/u/009.jpg) no-repeat center;"
            ),
            Div(
                H1("Welcome to the Vassar Family Genealogy Hub", cls="f1 lh-title"),
                P(
                    "Discover the rich history of the Vassar family as we journey through generations, tracing our roots back to the communities in and around Birmingham and Athens, Alabama. This site serves as a gathering place for Vassar family members, a resource to learn about our shared heritage, and a platform to preserve the remarkable stories that have shaped our lineage.",
                    cls="common-font"
                ),
                P(
                    "At the heart of our family's legacy are the seven Vassar sisters, each with their own unique story and impact. Explore detailed profiles, family records, and historical documents as we celebrate their lives and the lives of those who came before them.",
                    cls="common-font"
                ),
                P(
                    "Whether you're here to learn, contribute, or connect with relatives, this site is dedicated to honoring the Vassar family's enduring history. Welcome to your family's story.",
                    cls="common-font"
                ),
                cls="center measure-wide f5 pv5 lh-copy ph2"
            ),
            cls="athelas"
        ),
        Div(
            I(cls="fas fa-info-circle w1", style="color:currentcolor"),
            Span("Disclaimer about the validity of the content of the site.", cls="lh-title ml3 common-font"),
            cls="flex items-center justify-center pa4 bg-lightest-blue navy"
        ),
        Article(
            Div(
                Div(
                    Header(
                        H3("Genealogical Narrative", cls="f2 fw7 lh-title mt0 mb3"),
                        H4("David Taylor", cls="f3 fw4 i lh-title mt0"),
                        cls="bb b--black-70 pv4"
                    ),
                    Section(
                        P(
                            "The origins of the Vassar family can be traced to the areas in and surrounding Birmingham and Athens Alabama. Records of earlier times\n\n"
                            "remain with this portion of the family yet in the South. The family is divided into two branches. The first is the offspring of a union between a plantation owner and slave master by the name of Minges and a slave woman whose origins and name are yet unknown. Out of this union came Carol Minges (b. August 14, 1860) and Alice Minges (b. 1869). It is not known whether they were slave or free. Presumably after emancipation the same slave woman married James Vassar from Athens, Alabama.",
                            cls="times lh-copy measure f4 mt0 common-font"
                        ),
                        A("Read More", cls="f6 link dim br1 ph3 pv2 mb2 dib white bg-dark-blue", href="#0"),
                        cls="pt5 pb4"
                    ),
                    cls="fl pa3 pa4-ns black-70 f3 times",
                    style="background-color: #181C25"

                ),
                cls="cf",
                style="background: url(https://media.istockphoto.com/id/1510502412/photo/sunrise-over-lush-alabama-forest-and-lakelands.jpg?s=2048x2048&w=is&k=20&c=J93rsKAVQJPsaYpEu05eku7Evp2386k50v5hLvNRk2k=) no-repeat center center fixed; background-size: cover;"
            ),
            data_name="article-full-bleed-background"
        ),
        Section(
            Div(
                Div(
                    Div(
                        H2("Genealogical Map", cls="fw4 blue mt0 mb3"),
                        P(
                            "Discover the roots of the Vassar family with our interactive genealogical map. Trace the branches of our lineage, explore connections across generations, and see how each family member plays a part in our rich history. Start your journey through time and uncover the story of our ancestors!\n\n",
                            cls="black-70 measure lh-copy mv0 common-font"
                        ),
                        cls="pa3 pa4-ns dtc-ns v-mid"
                    ),
                    Div(
                        A(
                            "View Map",
                            href="#",
                            cls="no-underline f6 tc db w-100 pv3 bg-animate bg-blue hover-bg-dark-blue white br2"
                        ),
                        cls="pa3 pa4-ns dtc-ns v-mid"
                    ),
                    cls="dt-ns dt--fixed-ns w-100"
                ),
                cls=" center br2 ba b--light-blue bg-lightest-blue"
            ),
        ),
        Article(
            Div(
                Div(
                    Header(
                        P(
                            "At the heart of the Vassar family legacy are the seven remarkable sisters whose lives have shaped our family's history. Each sister has a unique story, filled with resilience, love, and dedication, reflecting the strength of our heritage. In this section, you'll find detailed profiles of these women, honoring their contributions to the family and the generations that followed. Explore their stories and gain deeper insight into the individuals who helped build the Vassar legacy.",
                            cls="times lh-copy measure f4 mt0 common-font"
                        ),
                        A("Read More", cls="f6 link dim br1 ph3 pv2 mb2 dib white bg-dark-blue", href="#0"),
                        cls="pt5 pb4"
                    ),
                    cls="fr pa3 pa4-ns black-70 measure-narrow f3 times",
                    style="background-color: #181C25"
                ),
                        H3("Learn more about the Vassar Sisters", cls="f2 fw7 lh-title mt0 mb3"),
                        cls="bb b--black-70 pv4"
                    ),
                    Section(
                cls="cf",
                style="background: url(https://i.pinimg.com/1200x/98/ba/9a/98ba9a87f66fef80069d3803e5b87de6.jpg) no-repeat center center fixed; background-size: cover;"
            )),
        cls="container")

history_routes(app)