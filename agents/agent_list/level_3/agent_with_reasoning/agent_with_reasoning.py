
import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools


# Load .env from the same folder as this script
from pathlib import Path
dotenv_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=dotenv_path)
openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    raise RuntimeError("OPENAI_API_KEY not found in .env file. Please add it and try again.")
os.environ['OPENAI_API_KEY'] = openai_api_key

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini", api_key=openai_api_key),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        ),
    ],
    instructions=[
        "Use tables to display data.",
        "Include sources in your response.",
        "Only include the report in your response. No other text.",
    ],
    markdown=True,
)
response = agent.print_response(
    "Write a report on NVDA",
    stream=True,
    show_full_reasoning=True,
    stream_intermediate_steps=True,
)
with open("response.txt", "w", encoding="utf-8") as f:
    f.write(str(response) + "\n")
