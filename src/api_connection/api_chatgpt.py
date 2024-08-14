import openai
from .LLM_interface import LLM
from .LLM_factory import LLMFactory

class ChatGPTApi(LLM):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.configure(api_key=api_key)

    def configure(self, **kwargs):
        openai.api_key = kwargs['api_key']

    def send_prompt(self, prompt: list) -> dict:
        response = openai.chat.completions.create(
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

    def factory_method(self) -> LLM:
        return ChatGPTApi(self.api_key)