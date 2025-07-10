import os # Standar library for Os operations
from dotenv import load_dotenv # loads environment variables from a .env file 

load_dotenv(os.path.join(os.path.dirname(__file__), '../../../.env')) #loads .env file for Api keys

from agno.agent import Agent # importing the agent class de Agno
from agno.models.openai import OpenAIChat # importing openai chat model  
from agno.tools.yfinance import YFinanceTools # imports yahoo finance tools

agent = Agent( # instance of agent
    model=OpenAIChat(id='gpt-4o'), # using gpt4o as the model 
    tools=[YFinanceTools(stock_price=True)], # adds a tool for getting prices 
    instructions=[ # intructions for the agntes behavior 
        "Use tables to display data.", 
        "Only include the table in your response. No other text.",
    ],
    markdown=True, # format output as markdown 
)
agent.print_response("What is the stock price of Apple?", stream=True) # the input

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
