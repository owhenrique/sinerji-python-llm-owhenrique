from abc import ABC, abstractmethod

class LLM(ABC):
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