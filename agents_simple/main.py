from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_default_openai_client,
    set_tracing_disabled,
    OpenAIChatCompletionsModel,
)

external_client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/", api_key=api_key
)

set_default_openai_client(external_client)

set_tracing_disabled(True)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash", openai_client=external_client
)
agent = Agent(
    name="HelloAgent", instructions="You are a helpful assistant.", model=model
)

result = Runner.run_sync(starting_agent=agent, input="Hello AI Agent")

print(result)