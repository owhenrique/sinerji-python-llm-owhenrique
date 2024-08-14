import os
import argparse
import pytest
from unittest.mock import patch, mock_open
import configparser
from .cli import CLI

class TestCLI:

    @patch('builtins.open', new_callable=mock_open, read_data="[API_KEYS]\nGEMINI_API_KEY=test_gemini_key\nCHATGPT_API_KEY=test_chatgpt_key")
    def test_load_config(self, mock_file):
        cli = CLI()
        cli.load_config()
        
        # Verifique se a configuração foi lida corretamente
        assert cli.config.get("API_KEYS", "GEMINI_API_KEY") == "test_gemini_key"
        assert cli.config.get("API_KEYS", "CHATGPT_API_KEY") == "test_chatgpt_key"

    @patch('argparse.ArgumentParser.parse_args')
    def test_parse_arguments(self, mock_parse_args):
        mock_parse_args.return_value = argparse.Namespace(
            prompt="What is AI?", 
            strategy="word_count", 
            keywords=None
        )
        cli = CLI()
        cli.parse_arguments()

        assert cli.args.prompt == "What is AI?"
        assert cli.args.strategy == "word_count"
        assert cli.args.keywords is None

    @patch.dict(os.environ, {"GEMINI_API_KEY": "env_gemini_key", "CHATGPT_API_KEY": "env_chatgpt_key"})
    def test_load_environment(self):
        cli = CLI()
        cli.load_environment()

        assert os.getenv("GEMINI_API_KEY") == "env_gemini_key"
        assert os.getenv("CHATGPT_API_KEY") == "env_chatgpt_key"

    def test_get_api_keys(self):
        cli = CLI()
        cli.config = configparser.ConfigParser()
        cli.config["API_KEYS"] = {
            "GEMINI_API_KEY": "test_gemini_key",
            "CHATGPT_API_KEY": "test_chatgpt_key"
        }

        gemini_key, chatgpt_key = cli.get_api_keys()
        assert gemini_key == "test_gemini_key"
        assert chatgpt_key == "test_chatgpt_key"

    @patch('argparse.ArgumentParser.parse_args')
    def test_get_prompt(self, mock_parse_args):
        mock_parse_args.return_value = argparse.Namespace(
            prompt="What is AI?", 
            strategy="word_count", 
            keywords=None
        )
        cli = CLI()
        cli.parse_arguments()

        assert cli.get_prompt() == "What is AI?"

    @patch('argparse.ArgumentParser.parse_args')
    def test_get_strategy(self, mock_parse_args):
        mock_parse_args.return_value = argparse.Namespace(
            prompt="What is AI?", 
            strategy="keyword_presence", 
            keywords=["AI", "machine learning"]
        )
        cli = CLI()
        cli.parse_arguments()

        assert cli.get_strategy() == "keyword_presence"

    @patch('argparse.ArgumentParser.parse_args')
    def test_get_keywords_success(self, mock_parse_args):
        mock_parse_args.return_value = argparse.Namespace(
            prompt="What is AI?", 
            strategy="keyword_presence", 
            keywords=["AI", "machine learning"]
        )
        cli = CLI()
        cli.parse_arguments()

        assert cli.get_keywords() == ["AI", "machine learning"]

    @patch('argparse.ArgumentParser.parse_args')
    def test_get_keywords_failure(self, mock_parse_args):
        mock_parse_args.return_value = argparse.Namespace(
            prompt="What is AI?", 
            strategy="keyword_presence", 
            keywords=None
        )
        cli = CLI()
        cli.parse_arguments()

        with pytest.raises(ValueError) as exc_info:
            cli.get_keywords()

        assert str(exc_info.value) == "Keywords must be provided when using 'keyword_presence' strategy."

