import pytest
from unittest.mock import MagicMock
from .command import SendPromptCommand, Invoker
from api_connection.factory import LLMFactory
from response_processing.strategy import EvaluationStrategy

class TestSendPromptCommand:
    def test_successful_execute(self):
        mock_factory = MagicMock(spec=LLMFactory)
        mock_llm = MagicMock()
        mock_strategy = MagicMock(spec=EvaluationStrategy)

        mock_factory.factory_method.return_value = mock_llm
        mock_llm.send_prompt.return_value = {'content': 'Test response'}
        mock_strategy.evaluate.return_value = 10.0

        command = SendPromptCommand(
            api_name="TestAPI",
            llm_factory=mock_factory,
            prompt=[{"role": "user", "content": "Hello"}],
            strategy=mock_strategy
        )

        result = command.execute()

        assert result['api_name'] == "TestAPI"
        assert result['response'] == {'content': 'Test response'}
        assert result['score'] == 10.0

    def test_failed_execute(self):
        mock_factory = MagicMock(spec=LLMFactory)
        mock_llm = MagicMock()
        mock_strategy = MagicMock(spec=EvaluationStrategy)

        mock_factory.factory_method.return_value = mock_llm
        mock_llm.send_prompt.side_effect = Exception("API Error")

        command = SendPromptCommand(
            api_name="TestAPI",
            llm_factory=mock_factory,
            prompt=[{"role": "user", "content": "Hello"}],
            strategy=mock_strategy
        )

        with pytest.raises(Exception) as exc_info:
            command.execute()

        assert str(exc_info.value) == "API Error"

class TestInvoker:
    def test_successful_execute_commands(self):
        mock_command1 = MagicMock(spec=SendPromptCommand)
        mock_command2 = MagicMock(spec=SendPromptCommand)

        mock_command1.execute.return_value = {"api_name": "TestAPI1", "response": "Response1", "score": 10.0}
        mock_command2.execute.return_value = {"api_name": "TestAPI2", "response": "Response2", "score": 8.5}

        invoker = Invoker()
        invoker.add_command(mock_command1)
        invoker.add_command(mock_command2)

        results = invoker.execute_commands()

        assert results == [
            {"api_name": "TestAPI1", "response": "Response1", "score": 10.0},
            {"api_name": "TestAPI2", "response": "Response2", "score": 8.5}
        ]

    def test_failed_execute_commands(self):
        mock_command1 = MagicMock(spec=SendPromptCommand)
        mock_command2 = MagicMock(spec=SendPromptCommand)

        mock_command1.execute.return_value = {"api_name": "TestAPI1", "response": "Response1", "score": 10.0}
        mock_command2.execute.side_effect = Exception("Command Error")

        invoker = Invoker()
        invoker.add_command(mock_command1)
        invoker.add_command(mock_command2)

        with pytest.raises(Exception) as exc_info:
            invoker.execute_commands()

        assert str(exc_info.value) == "Command Error"
