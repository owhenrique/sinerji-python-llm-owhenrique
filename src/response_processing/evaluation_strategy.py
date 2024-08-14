from abc import ABC, abstractmethod

class EvaluationStrategy(ABC):
    """
    A interface Strategy declara a operação comum a todas as estratégias de
    avaliação de respostas.
    """
    @abstractmethod
    def evaluate(self, response: dict) -> float:
        pass