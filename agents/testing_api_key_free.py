import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

from agno.agent import Agent
from textwrap import dedent

# Model classes
GroqChat = None
DeepSeekChat = None
GeminiChat = None
try:
    from agno.models.groq import GroqChat
except Exception:
    GroqChat = None
try:
    from agno.models.deepseek import DeepSeekChat
except Exception:
    DeepSeekChat = None
# GeminiChat import is commented out because agno.models.gemini could not be resolved
# try:
#     from agno.models.gemini import GeminiChat
# except Exception:
#     GeminiChat = None

# List of models to test
Models = []

if GroqChat:
    groq_api_key = os.getenv("GROQ_API_KEY")
    Models.extend([
        ("Groq LLaMA3-70B", GroqChat(id="llama3-70b-8192", api_key=groq_api_key)),
        ("Groq Mixtral", GroqChat(id="mixtral-8x7b-32768", api_key=groq_api_key)),
    ])
if DeepSeekChat:
    deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
    Models.append(("DeepSeek Chat", DeepSeekChat(id="deepseek-chat", api_key=deepseek_api_key)))
# GeminiChat is not available in your agno version, so it is skipped

Test_prompt = "Explain in simple terms what an autonomous AI agent is, and give one example."


def test_models():
    for model_name, model in Models:
        print(f"\n🧪 Testing model: {model_name}")
        try:
            agent = Agent(model=model, markdown=True)
            response = agent.run(Test_prompt, stream=False)
            print(f"Response from {model_name}:\n{response}\n")
            print("✅ Response:\n", response)
            print("-" * 80)
        except Exception as e:
            print(f"❌ Error occurred while testing {model_name}: {e}")
            print("Continuing to next model...\n")

if __name__ == "__main__":
    test_models()
    print("All models tested (errors above are expected if API keys are missing or invalid).")