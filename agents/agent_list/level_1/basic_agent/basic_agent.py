import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '../../.env'))

from agno.agent import Agent
from agno.models.openai import OpenAIChat

# Use GPT-4o model
agent = Agent(model=OpenAIChat(id="gpt-4o"), markdown=True)

# Ask multiple questions
questions = [
    "What is the stock price of Apple?",
    "Who is the CEO of Microsoft?",
    "Summarize the latest news about Tesla.",
    "What are the top 3 programming languages in 2025?",
    "شنو هي أحسن مدينة في المغرب؟"  # Darija: What is the best city in Morocco?
]

output_path = os.path.join(os.path.dirname(__file__), "responses_darija.txt")

with open(output_path, "w", encoding="utf-8") as f:
    for q in questions:
        print(f"\nQuestion: {q}")
        f.write(f"Question: {q}\n")
        response = ""
        for chunk in agent.run(q, stream=True):
            # Only write content if the event has 'content' attribute
            content = getattr(chunk, 'content', None)
            if content:
                print(content, end="", flush=True)
                f.write(content)
                response += content
        f.write("\n\n")
