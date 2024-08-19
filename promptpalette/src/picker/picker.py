from typing import List, Dict, Union, Optional, Literal
from ..kb.kb import PromptKnowledge
from .prompt import picker_prompt
from .schema import PickerOutput
# from promptpalette._client import LLMFactory


class Picker:

    def __init__(self, llm_factory, provider: Literal["openai", "claude"],
                 model_name: str, **kwargs) -> None:

        self.llm = llm_factory
        self.model_name = model_name
        self.provider = provider

    async def __call__(self, requirements_objectives: str):
        messages = [{
            "role": "system",
            "content": picker_prompt
        }, {
            "role":
            "user",
            "content":
            f"""Requirements and Objectives: ```{requirements_objectives}```\n\nPrompt Corpus\n<prompt-corpus>\n{PromptKnowledge.PromptKnowledge}\n</prompt-corpus>"""
        }]
        tools = [{
            "name": "analyzeAndFetchRelevantPrompts",
            "parameters": PickerOutput.model_json_schema()
        }]
        return await getattr(self.llm, self.provider).__tool__(
            self.model_name,
            messages,
            tools,
            tool_choice={"name": "analyzeAndFetchRelevantPrompts"})
