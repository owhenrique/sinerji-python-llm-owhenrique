from abc import ABC, abstractmethod
from api_connection.LLM_factory import LLMFactory
from response_processing.evaluation_strategy import EvaluationStrategy

class Command(ABC):
    @abstractmethod
    def execute(self) -> dict:
        pass

class SendPromptCommand(Command):
    """
    Command para enviar um prompt a um LLM específico e avaliar a resposta.
    """
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
    """
    O Invoker configura e executa os comandos. Pode também permitir o
    encadeamento de comandos.
    """
    def __init__(self):
        self._commands = []

    def add_command(self, command: Command):
        self._commands.append(command)

    def execute_commands(self):
        results = []
        for command in self._commands:
            results.append(command.execute())
        return results
