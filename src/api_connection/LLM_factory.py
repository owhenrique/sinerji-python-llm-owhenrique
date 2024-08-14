from abc import ABC, abstractmethod
from .LLM_interface import LLM

class LLMFactory(ABC):
    """
    A classe LLMFactory declara o factory method que deve retornar um objeto
    do tipo LLM (Language Model). As subclasses geralmente implementam este método.
    """
    @abstractmethod
    def factory_method(self) -> LLM:
        pass
    
    def send_prompt(self, prompt: str) -> dict:
        llm = self.factory_method()
        return llm.send_prompt(prompt)
