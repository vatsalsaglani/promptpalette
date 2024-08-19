import json
from typing import Dict, List
from .base import BaseLLM
from anthropic import AsyncAnthropic, AsyncAnthropicBedrock


class ClaudeLLM(BaseLLM):

    def __init__(self, api_key: str, **kwargs) -> None:
        super().__init__()
        if kwargs.get("api_provider", "") == "bedrock":
            assert "aws_access_key" in kwargs and "aws_region" in kwargs and "aws_secret_key" in kwargs, "When choosing bedrock `aws_region`, `aws_access_key` and `aws_secret_key` keyword arguments are required. Please verify if those are provided with the right values."
            self.client = AsyncAnthropicBedrock(
                aws_access_key=kwargs.get("aws_access_key"),
                aws_region=kwargs.get("aws_region"),
                aws_secret_key=kwargs.get("aws_secret_key"))
        else:
            self.client = AsyncAnthropic(api_key=api_key)

    async def __complete__(self,
                           model_name: str,
                           messages: List[Dict],
                           max_tokens: int | None = 4096,
                           temperature: int | None = 0.2,
                           is_function_call: bool | None = False,
                           **kwargs):
        system_message = list(
            filter(lambda message: message.get("role") == "system", messages))
        if len(system_message) > 0:
            system_message = system_message[0].get("content")
            messages = list(
                filter(lambda message: message.get("role") != "system",
                       messages))
        else:
            system_message = None
        if system_message:
            kwargs["system"] = system_message
        output = await self.client.messages.create(messages=messages,
                                                   model=model_name,
                                                   max_tokens=max_tokens,
                                                   temperature=temperature,
                                                   **kwargs)
        if is_function_call:
            return output.content[0]
        return output.content[0].text

    async def __tool__(self,
                       model_name: str,
                       messages: List[Dict],
                       tools: List[Dict],
                       tool_choice: Dict | None = None,
                       max_tokens: int | None = 4096,
                       temperature: int | None = 0.2,
                       **kwargs):
        system_message = list(
            filter(lambda message: message.get("role") == "system", messages))
        if len(system_message) > 0:
            system_message = system_message[0].get("content")
            messages = list(
                filter(lambda message: message.get("role") != "system",
                       messages))
        else:
            system_message = None
        if system_message:
            kwargs["system"] = system_message
        for tool in tools:
            if "parameters" in tool:
                tool["input_schema"] = tool["parameters"]
                del tool["parameters"]
        if tool_choice:
            tool_choice = {"type": "tool", "name": tool_choice.get("name")}
        else:
            tool_choice = {"type": "any"}
        tool_output = await self.__complete__(model_name,
                                              messages,
                                              max_tokens=max_tokens,
                                              temperature=temperature,
                                              tools=tools,
                                              tool_choice=tool_choice,
                                              is_function_call=True,
                                              **kwargs)
        if tool_output.input:
            arguments = None
            if isinstance(tool_output.input, str):
                arguments = json.loads(tool_output.input)
            else:
                arguments = tool_output.input
            tool_name = tool_output.name
            return [{"name": tool_name, "parameters": arguments}]
        return None
        # if tool_output.tool_calls:
        #     arguments = json.loads(tool_output.tool_calls.function.arguments)
        #     return arguments
        # return None

    async def __stream__(self,
                         model_name: str,
                         messages: List[Dict],
                         max_tokens: int | None = 4096,
                         temperature: int | None = 0.2,
                         **kwargs):
        system_message = list(
            filter(lambda message: message.get("role") == "system", messages))
        if len(system_message) > 0:
            system_message = system_message[0].get("content")
            messages = list(
                filter(lambda message: message.get("role") != "system",
                       messages))
        else:
            system_message = None
        if system_message:
            kwargs["system"] = system_message
        async with self.client.messages.stream(max_tokens=max_tokens,
                                               messages=messages,
                                               model=model_name,
                                               temperature=temperature,
                                               **kwargs) as stream:
            async for text in stream.text_stream:
                yield text

        # async for chunk in self.client.messages.create(messages,
        #                                                model_name,
        #                                                max_tokens=max_tokens,
        #                                                temperature=temperature,
        #                                                stream=True,
        #                                                **kwargs):
        #     if chunk.choices[0].delta.content is not None:
        #         yield chunk.choices[0].delta.content
