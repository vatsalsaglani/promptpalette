from .src.llm.claude import ClaudeLLM
from .src.llm.openai import OpenAILLM
from .src.picker import picker


class LLMFactory:

    def __init__(self, api_key, **kwargs) -> None:
        self.claude = ClaudeLLM(api_key, **kwargs)
        self.openai = OpenAILLM(api_key, **kwargs)
