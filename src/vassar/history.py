from fasthtml.components import Title, Main, H1, Article, Div, Header, P, A, H3, Section, H2, H4, Span, I, Blockquote, \
    Cite

from vassar.components import page_header, page_nav, page_footer

def history_routes(app):
    rt = app.route

    @rt("/history")
    def get():
        return (
            Title("The Vassar Community Project"),
            page_header(),
            page_nav(),
            Main(
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


                cls="container")
            ,
            page_footer(),
        )