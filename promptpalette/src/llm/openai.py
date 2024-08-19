import json
from typing import Dict, List
from .base import BaseLLM
from openai import AsyncOpenAI, AsyncAzureOpenAI


class OpenAILLM(BaseLLM):

    def __init__(self, api_key: str, **kwargs) -> None:
        super().__init__()
        if kwargs.get("api_provider", "") == "azure":
            assert "base_url" in kwargs and "openai_api_version" in kwargs, "When choosing azure `base_url` and `openai_api_version` keyword arguments are required. Please verify if those are provided with the right values along with the `api_key`."
            self.client = AsyncAzureOpenAI(
                azure_endpoint=kwargs.get("base_url"),
                api_key=api_key,
                api_version=kwargs.get("openai_api_version"))
        else:
            self.client = AsyncOpenAI(api_key=api_key)

    async def __complete__(self,
                           model_name: str,
                           messages: List[Dict],
                           max_tokens: int | None = 4096,
                           temperature: int | None = 0.2,
                           is_function_call: bool | None = False,
                           **kwargs):
        output = await self.client.chat.completions.create(
            messages=messages,
            model=model_name,
            max_tokens=max_tokens,
            temperature=temperature,
            **kwargs)
        if is_function_call:
            return output.choices[0].message
        return output.choices[0].message.content

    async def __tool__(self,
                       model_name: str,
                       messages: List[Dict],
                       tools: List[Dict],
                       tool_choice: Dict | None = None,
                       max_tokens: int | None = 4096,
                       temperature: int | None = 0.2,
                       **kwargs):
        formatted_tools = []
        for tool in tools:
            formatted_tools.append({"type": "function", "function": tool})
        if tool_choice:
            formatted_tool_choice = {
                "type": "function",
                "function": {
                    "name": tool_choice
                }
            }
        else:
            formatted_tool_choice = None
        tool_output = await self.__complete__(
            model_name=model_name,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            tools=formatted_tools,
            tool_choice=formatted_tool_choice,
            is_function_call=True,
            **kwargs)
        # print(f"TOOL OUTPUT: {tool_output}")
        if tool_output.tool_calls:
            to = []
            for tc in tool_output.tool_calls:
                to.append({
                    "name": tc.function.name,
                    "parameters": json.loads(tc.function.arguments)
                })
            return to
        return None

    async def __stream__(self,
                         model_name: str,
                         messages: List[Dict],
                         max_tokens: int | None = 4096,
                         temperature: int | None = 0.2,
                         **kwargs):
        stream_gen = await self.client.chat.completions.create(
            messages=messages,
            model=model_name,
            max_tokens=max_tokens,
            temperature=temperature,
            stream=True,
            **kwargs)
        async for chunk in stream_gen:
            if chunk.choices[0].delta.content is not None:
                yield chunk.choices[0].delta.content
