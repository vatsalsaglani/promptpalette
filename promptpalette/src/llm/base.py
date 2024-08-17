from abc import ABC, abstractmethod
from typing import List, Dict, Union, Optional


class BaseLLM(ABC):

    @abstractmethod
    async def __tool__(self,
                       model_name: str,
                       messages: List[Dict],
                       tools: List[Dict],
                       tool_choice: Optional[Dict] = None,
                       max_tokens: Optional[int] = 4096,
                       temperature: Optional[int] = 0.2,
                       **kwargs):
        pass

    @abstractmethod
    async def __complete__(self,
                           model_name: str,
                           messages: List[Dict],
                           max_tokens: Optional[int] = 4096,
                           temperature: Optional[int] = 0.2,
                           **kwargs):
        pass

    @abstractmethod
    async def __stream__(self,
                         model_name: str,
                         messages: List[Dict],
                         max_tokens: Optional[int] = 4096,
                         temperature: Optional[int] = 0.2,
                         **kwargs):
        pass
