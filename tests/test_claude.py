import asyncio
from promptpalette.src.llm.claude import ClaudeLLM
from pydantic import BaseModel


class Weather(BaseModel):
    city_name: str


api_key = "YOUR CLAUDE API KEY"

llm = ClaudeLLM(api_key=api_key)

messages = [{
    "role": "system",
    "content": "Call the appropriate tool for getting weather."
}, {
    "role": "user",
    "content": "What's the weather in Bangalore India."
}]

tools = [{"name": "getWeather", "parameters": Weather.model_json_schema()}]

print(asyncio.run(llm.__tool__("claude-3-5-sonnet-20240620", messages, tools)))

print(asyncio.run(llm.__complete__("claude-3-5-sonnet-20240620", messages)))


async def stream():
    async for chunk in llm.__stream__("claude-3-5-sonnet-20240620", messages):
        print(chunk, end="", flush=True)


asyncio.run(stream())
