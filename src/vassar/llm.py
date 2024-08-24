from instruct_easy import SystemMessage, LLMModel, prompt
from pydantic import BaseModel, Field
from rich.console import Console

console = Console()


class CypherQueryData(BaseModel):
    query: str = Field(..., description="The Cypher query to be executed.")
    description: str = Field(..., description="A description of the Cypher query.")
    detailed_explanation: str = Field(
        ..., description="A detailed explanation of the Cypher query."
    )


CYPHER_EXPERT_CTX = [
    SystemMessage(
        content="You are a Neo4j Cypher master!"
        "You will assist in generating Cypher queries based on the schema of the database."
        "The queries will be used to create, read, update, and delete data in the database."
        "You will also assist in generating Cypher queries to retrieve the schema of the database."
        "Be sure to review the schema of the database before generating queries."
        "Be helpful, and good luck!"
    )
]


@prompt(
    context=CYPHER_EXPERT_CTX,
    model=LLMModel.Claude35_Sonnet,
)
def gen_cypher_query(_: str, input: CypherQueryData = None) -> str:
    console.log(f"DESCRIPTION::::{input.description}")
    console.log(f"DETAILED EXPLANATION::::{input.detailed_explanation}")
    query = input.query
    return query
