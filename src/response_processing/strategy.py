from abc import ABC, abstractmethod

class EvaluationStrategy(ABC):
    """
    A interface Strategy declara a operação comum a todas as estratégias de
    avaliação de respostas.
    """
    @abstractmethod
    def evaluate(self, response: dict) -> float:
        pass


class WordCountStrategy(EvaluationStrategy):
    """
    Esta estratégia avalia a resposta com base no número de palavras.
    """
    def evaluate(self, response: dict) -> float:
        return len(response['content'].split())


class KeywordPresenceStrategy(EvaluationStrategy):
    """
    Esta estratégia avalia a resposta com base na presença de palavras-chave.
    """
    def __init__(self, keywords: list):
        self.keywords = keywords

    def evaluate(self, response: dict) -> float:
        return sum(1 for word in self.keywords if word in response['content'])

