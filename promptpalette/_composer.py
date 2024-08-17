import json
from typing import List, Dict, Union, Optional, Literal
from .src.picker import Picker
from .src.writer import Writer
from . import LLMFactory


class Composer:

    def __init__(self, api_key: str, provider: Literal["openai", "claude"],
                 model_name: str, **kwargs):
        self.llmf = LLMFactory(api_key, **kwargs)
        self.picker = Picker(self.llmf,
                             provider=provider,
                             model_name=model_name,
                             **kwargs)
        self.writer = Writer(self.llmf,
                             provider=provider,
                             model_name=model_name,
                             **kwargs)

    async def __call__(self, requirements_objectives: str):
        picker_output = await self.picker(requirements_objectives)
        print(f"PICKER OUTPUT:\n{json.dumps(picker_output, indent=4)}")
        writer_output = await self.writer(requirements_objectives,
                                          picker_output)
        return writer_output
