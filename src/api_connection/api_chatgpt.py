import openai
from .factory import LLMInterface, LLMFactory

class ChatGPTApi(LLMInterface):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = None
        self.configure(api_key=api_key)

    def configure(self, **kwargs):
        self.client = openai.OpenAI(
            api_key=kwargs['api_key']
        )

    def send_prompt(self, prompt: list) -> dict:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=prompt,
            temperature=0.5,
            max_tokens=200
        )
        message_content = [response.choices[0].message.content]
        return {"prompt": prompt[0]['content'], "content": message_content[0], "usage": response.usage}

class ChatGPTFactory(LLMFactory):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def factory_method(self) -> LLMInterface:
        return ChatGPTApi(self.api_key)