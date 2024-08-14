import pytest
from unittest.mock import patch, MagicMock
from api_connection.factory import LLMFactory
from api_connection.api_chatgpt import ChatGPTApi, ChatGPTFactory

class TestChatGPTApi:
    @patch('openai.OpenAI')
    def test_successful_send_prompt(self, mock_openai):
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(message=MagicMock(content="Test response"))]
        mock_response.usage = {"tokens": 100}
        mock_client.chat.completions.create.return_value = mock_response
        mock_openai.return_value = mock_client

        api = ChatGPTApi(api_key="fake-api-key")
        prompt = [{"role": "user", "content": "Hello!"}]
        result = api.send_prompt(prompt)

        assert result["prompt"] == "Hello!"
        assert result["content"] == "Test response"
        assert result["usage"] == {"tokens": 100}

    @patch('openai.OpenAI')
    def test_failed_send_prompt(self, mock_openai):
        mock_client = MagicMock()
        mock_client.chat.completions.create.side_effect = Exception("API error")
        mock_openai.return_value = mock_client

        api = ChatGPTApi(api_key="fake-api-key")
        prompt = [{"role": "user", "content": "Hello!"}]

        with pytest.raises(Exception) as exc_info:
            api.send_prompt(prompt)

        assert str(exc_info.value) == "API error"

class TestChatGPTFactory:
    def test_successful_factory_method(self):
        factory = ChatGPTFactory(api_key="fake-api-key")
        api_instance = factory.factory_method()

        assert isinstance(api_instance, ChatGPTApi)
        assert api_instance.api_key == "fake-api-key"

    def test_failed_factory_method(self):
        with pytest.raises(TypeError):
            factory = ChatGPTFactory()
