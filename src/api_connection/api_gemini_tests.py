import pytest
from unittest.mock import patch, MagicMock
from api_connection.factory import LLMFactory
from api_connection.api_gemini import GeminiApi, GeminiFactory

class TestGeminiApi:

    @patch('google.generativeai.GenerativeModel')
    @patch('google.generativeai.configure')
    def test_successful_send_prompt(self, mock_configure, mock_model):
        # Mock do modelo e da resposta
        mock_model_instance = MagicMock()
        mock_response = MagicMock()
        mock_response.text = "Test response"
        mock_model_instance.generate_content.return_value = mock_response
        mock_model.return_value = mock_model_instance

        api = GeminiApi(api_key="fake-api-key")
        prompt = [{"role": "user", "content": "Hello!"}]
        result = api.send_prompt(prompt)

        assert result["prompt"] == "Hello!"
        assert result["content"] == "Test response"

    @patch('google.generativeai.GenerativeModel')
    @patch('google.generativeai.configure')
    def test_failed_send_prompt(self, mock_configure, mock_model):
        # Mock para simular uma exceção
        mock_model_instance = MagicMock()
        mock_model_instance.generate_content.side_effect = Exception("API error")
        mock_model.return_value = mock_model_instance

        api = GeminiApi(api_key="fake-api-key")
        prompt = [{"role": "user", "content": "Hello!"}]

        with pytest.raises(Exception) as exc_info:
            api.send_prompt(prompt)

        assert str(exc_info.value) == "API error"

class TestGeminiFactory:

    def test_successful_factory_method(self):
        factory = GeminiFactory(api_key="fake-api-key")
        api_instance = factory.factory_method()

        assert isinstance(api_instance, GeminiApi)
        assert api_instance.api_key == "fake-api-key"

    def test_failed_factory_method(self):
        # Exemplo de falha quando a API key não é passada corretamente
        with pytest.raises(TypeError):
            factory = GeminiFactory()  # Falha porque api_key é obrigatória