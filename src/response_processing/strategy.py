from abc import ABC, abstractmethod

class EvaluationStrategy(ABC):
    @abstractmethod
    def evaluate(self, response: dict) -> float:
        pass

class WordCountStrategy(EvaluationStrategy):
    def evaluate(self, response: dict) -> float:
        return len(response['content'].split())

class KeywordPresenceStrategy(EvaluationStrategy):
    def __init__(self, keywords: list):
        self.keywords = keywords

    def evaluate(self, response: dict) -> float:
        return sum(1 for word in self.keywords if word in response['content'])

