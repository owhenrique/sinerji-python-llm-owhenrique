from abc import ABC, abstractmethod
from api_connection.factory import LLMFactory
from response_processing.strategy import EvaluationStrategy

class Command(ABC):
    @abstractmethod
    def execute(self) -> dict:
        pass

class SendPromptCommand(Command):
    def __init__(self, api_name: str, llm_factory: LLMFactory, prompt: list, strategy: EvaluationStrategy):
        self.api_name = api_name
        self.llm_factory = llm_factory
        self.prompt = prompt
        self.strategy = strategy

    def execute(self) -> dict:
        llm = self.llm_factory.factory_method()
        response = llm.send_prompt(self.prompt)
        evaluation_score = self.strategy.evaluate(response)
        return {"api_name": self.api_name, "response": response, "score": evaluation_score}


class Invoker:
    def __init__(self):
        self._commands = []

    def add_command(self, command: Command):
        self._commands.append(command)

    def execute_commands(self):
        results = []
        for command in self._commands:
            results.append(command.execute())
        return results
