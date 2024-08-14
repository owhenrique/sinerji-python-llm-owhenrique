from abc import ABC, abstractmethod

class LLMInterface(ABC):
    """
    A interface LLM declara a operação que todos os modelos de linguagem devem implementar.
    """  
    @abstractmethod
    def send_prompt(self, prompt: list) -> dict:
        pass
    
    @abstractmethod
    def configure(self, **kwargs):
        """
        Método opcional para configuração de parâmetros adicionais para o modelo de linguagem.
        """
        pass

class LLMFactory(ABC):
    """
    A classe LLMFactory declara o factory method que deve retornar um objeto
    do tipo LLM (Language Model). As subclasses geralmente implementam este método.
    """
    @abstractmethod
    def factory_method(self) -> LLMInterface:
        pass
    
    def send_prompt(self, prompt: str) -> dict:
        llm = self.factory_method()
        return llm.send_prompt(prompt)
