import asyncio
from promptpalette.src.llm.openai import OpenAILLM
from pydantic import BaseModel


class Weather(BaseModel):
    city_name: str


api_key = "YOUR OPENAI API KEY"

llm = OpenAILLM(api_key=api_key)

messages = [{
    "role": "system",
    "content": "Call the appropriate tool for getting weather."
}, {
    "role": "user",
    "content": "What's the weather in Bangalore India."
}]

tools = [{"name": "getWeather", "parameters": Weather.model_json_schema()}]

print(asyncio.run(llm.__tool__("gpt-4o-mini", messages, tools)))

print(asyncio.run(llm.__complete__("gpt-4o-mini", messages)))


async def stream():
    async for chunk in llm.__stream__("gpt-4o-mini", messages):
        print(chunk, end="", flush=True)


asyncio.run(stream())
