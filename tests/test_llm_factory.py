import asyncio
from promptpalette import LLMFactory
from pydantic import BaseModel


class Weather(BaseModel):
    city_name: str


messages = [{
    "role": "system",
    "content": "Call the appropriate tool for getting weather."
}, {
    "role": "user",
    "content": "What's the weather in Bangalore India."
}]

tools = [{"name": "getWeather", "parameters": Weather.model_json_schema()}]

# openai
api_key = "YOUR OPENAI API KEY"
llm = LLMFactory(api_key)

provider = "openai"
model_name = "gpt-4o-mini"

print(asyncio.run(
    getattr(llm, provider).__tool__(model_name, messages, tools)))

print(asyncio.run(getattr(llm, provider).__complete__(model_name, messages)))


async def stream():
    async for chunk in getattr(llm, provider).__stream__(model_name, messages):
        print(chunk, end="", flush=True)


asyncio.run(stream())

print()

# claude

api_key = "YOUR CLAUDE API KEY"
llm = LLMFactory(api_key)

provider = "claude"
model_name = "claude-3-5-sonnet-20240620"

print(asyncio.run(
    getattr(llm, provider).__tool__(model_name, messages, tools)))

print(asyncio.run(getattr(llm, provider).__complete__(model_name, messages)))


async def stream():
    async for chunk in getattr(llm, provider).__stream__(model_name, messages):
        print(chunk, end="", flush=True)


asyncio.run(stream())

print()
