import argparse
import configparser
import logging
import os
from dotenv import load_dotenv
class CLI:
    def __init__(self):
        self.config = None
        self.args = None
        self.setup_logging()

    def setup_logging(self):
        #logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        pass

    def parse_arguments(self):
        parser = argparse.ArgumentParser(
            description="Send questions to different language models.",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )
        
        parser.add_argument("prompt", type=str, help="The question to be sent to the language models.")
        parser.add_argument(
            "--strategy", 
            "--stg",
            type=str, 
            choices=["word_count", "keyword_presence"], 
            default="word_count",
            help="The evaluation strategy to be used."
        )
        parser.add_argument(
            "--keywords", 
            "--kws",
            type=str, 
            nargs='+', 
            help="Keywords to be used if 'keyword_presence' strategy is selected."
        )
        
        self.args = parser.parse_args()

    def load_config(self):
        self.config = configparser.ConfigParser()
        self.config.read("../config.ini")

    def load_environment(self):
        load_dotenv()

    def get_api_keys(self):
        gemini_api_key = self.config.get("API_KEYS", "GEMINI_API_KEY")
        chatgpt_api_key = self.config.get("API_KEYS", "CHATGPT_API_KEY")
        return gemini_api_key, chatgpt_api_key

    def get_prompt(self):
        return self.args.prompt

    def get_strategy(self):
        return self.args.strategy

    def get_keywords(self):
        if self.args.strategy == "keyword_presence":
            if not self.args.keywords:
                raise ValueError("Keywords must be provided when using 'keyword_presence' strategy.")
            return self.args.keywords
        return None