from typing import Any, List, Dict, Union, Optional, Literal
from ..kb.kb import PromptKnowledge
from .prompt import writer_prompt


class Writer:

    def __init__(self, llm_factory, provider: Literal["openai", "claude"],
                 model_name: str, **kwargs) -> None:

        self.llm = llm_factory
        self.model_name = model_name
        self.provider = provider

    async def __call__(self, requirements_objectives: str,
                       picker_output: List[Dict]):
        recommended_prompting_strategies = picker_output[0].get(
            "parameters").get("prompt_recommendations")
        prompt_examples = ""
        for prompt_strategy in recommended_prompting_strategies:
            if prompt_strategy in PromptKnowledge.PromptExamples:
                prompt_examples += f"{PromptKnowledge.PromptExamples[prompt_strategy]}\n"
        prompt_examples = f"<recommended-prompts>\n{prompt_examples}\n</recommended-prompts>"
        messages = [{
            "role": "system",
            "content": writer_prompt
        }, {
            "role":
            "user",
            "content":
            f"""Requirements and Objectives: ```{requirements_objectives}```\n\nPrompt Strategies and Examples\n{prompt_examples}"""
        }]
        return await getattr(self.llm, self.provider).__complete__(
            self.model_name, messages)
