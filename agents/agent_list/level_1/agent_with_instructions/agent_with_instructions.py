import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '../../../.env'))

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=OpenAIChat(id='gpt-4o'),
    tools=[YFinanceTools(stock_price=True)],
    instructions=[
        "Use tables to display data.",
        "Only include the table in your response. No other text.",
    ],
    markdown=True,
)
agent.print_response("What is the stock price of Apple?", stream=True)

# ## ┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                                                                     ┃
# ┃ What is the stock price of Apple?                                                                                                   ┃
# ┃                                                                                                                                     ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# ┏━ Tool Calls ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                                                                     ┃
# ┃ • get_current_stock_price(symbol=AAPL)                                                                                              ┃
# ┃                                                                                                                                     ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
# ┏━ Response (6.3s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                                                                     ┃
# ┃                                                                                                                                     ┃
# ┃                                                                                                                                     ┃
# ┃   Stock Symbol   Company Name   Current Stock Price                                                                                 ┃
# ┃  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                                                                ┃
# ┃   AAPL           Apple Inc.     $200.67                                                                                             ┃
