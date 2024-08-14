from abc import ABC, abstractmethod

class LLMInterface(ABC): 
    @abstractmethod
    def send_prompt(self, prompt: list) -> dict:
        pass
    
    @abstractmethod
    def configure(self, **kwargs):
        pass

class LLMFactory(ABC):
    @abstractmethod
    def factory_method(self) -> LLMInterface:
        pass
    
    def send_prompt(self, prompt: str) -> dict:
        llm = self.factory_method()
        return llm.send_prompt(prompt)
