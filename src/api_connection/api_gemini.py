import google.generativeai as genai
from .factory import LLMInterface, LLMFactory

class GeminiApi(LLMInterface):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.model = None
        self.configure(api_key=api_key)

    def configure(self, **kwargs):
        genai.configure(api_key=kwargs['api_key'])
        self.model = genai.GenerativeModel('gemini-1.5-flash-latest')
        genai.GenerationConfig(
            temperature=0.5,
            max_output_tokens=500
        )

    def send_prompt(self, prompt: list) -> dict:
        response = self.model.generate_content(
            str(prompt[0]),
        )
        message_content = response.text
        return {"prompt": prompt[0]['content'], "content": message_content}

class GeminiFactory(LLMFactory):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def factory_method(self) -> LLMInterface:
        return GeminiApi(self.api_key)