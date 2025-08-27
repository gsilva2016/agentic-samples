import os
import asyncio
import litellm
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm 
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
from litellm import completion
from .tools_mockup import *
from dotenv import load_dotenv

# Load ENV settings
load_dotenv()
agent_model_endpoint = os.getenv("AGENT_MODEL_ENDPOINT", "http://localhost:8013/v3")
agent_model_name = os.getenv("AGENT_MODEL_NAME", "")
agent_model_device = os.getenv("AGENT_MODEL_DEVICE", "GPU")
agent_instruction = os.getenv("AGENT_INSTRUCTION", "")

# Enable DEBUG
litellm._turn_on_debug()

# Connecct model server endpoint
llm_serving = LiteLlm(
    model = agent_model_name,
    api_base = agent_model_endpoint,
    api_key="none",
    additional_drop_params=["extra_body"]
)

# Create an agent which can use multiple tools to take its action. 
# Note ADKWEB requires root_agent object
root_agent = Agent(
    name = "pos_agent",
    model = llm_serving,
    description = "Multimodal AI agent improves operational efficiency for POS stations",
    instruction = agent_instruction,
    tools=[get_pos_transaction_data, get_pos_ai_analytics_transaction_data],
)
