import os
from dotenv import load_dotenv
from pathlib import Path
from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.url import UrlKnowledge
from agno.models.openai import OpenAIChat
from agno.tools.reasoning import ReasoningTools
from agno.vectordb.lancedb import LanceDb, SearchType
# Load environment variables from the global .env file in the agents root
AGENTS_ROOT = Path(__file__).resolve().parents[3]
env_path = AGENTS_ROOT / '.env'
load_dotenv(dotenv_path=env_path)

# Check for OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise EnvironmentError(f"OPENAI_API_KEY is missing. Please set it in your global .env file at {env_path}.")

# Load Agno documentation in a knowledge base
knowledge = UrlKnowledge(
    urls=["https://docs.agno.com/introduction/agents.md"],
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="agno_docs",
        search_type=SearchType.hybrid,
        # Use OpenAI for embeddings
        embedder=OpenAIEmbedder(id="text-embedding-3-small", dimensions=1536),
    ),
)

agent = Agent(
    name="Agno Assist",
    model=OpenAIChat(id="gpt-4o"),  # Use GPT-4o, you can change to "gpt-3.5-turbo" if needed
    instructions=[
        "Use tables to display data.",
        "Include sources in your response.",
        "Search your knowledge before answering the question.",
        "Only include the output in your response. No other text.",
    ],
    knowledge=knowledge,
    tools=[ReasoningTools(add_instructions=True)],
    add_datetime_to_instructions=True,
    markdown=True,
)

if __name__ == "__main__":
    # Load the knowledge base, comment out after first run
    # Set recreate to True to recreate the knowledge base if needed
    if agent.knowledge is not None:
        agent.knowledge.load(recreate=False)
    else:
        raise ValueError("agent.knowledge is None. Please ensure the knowledge base is properly initialized.")

    agent.print_response(
        "What are Agents?",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )
