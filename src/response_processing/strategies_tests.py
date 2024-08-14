import pytest
from strategy import WordCountStrategy, KeywordPresenceStrategy

class TestWordCountStrategy:
    def test_successful_evaluate(self):
        strategy = WordCountStrategy()
        response = {'content': 'This is a test response with eight words.'}
        result = strategy.evaluate(response)
        assert result == 8

    def test_failed_evaluate(self):
        strategy = WordCountStrategy()
        response = {'content': ''}
        result = strategy.evaluate(response)
        assert result == 0

class TestKeywordPresenceStrategy:
    def test_successful_evaluate(self):
        strategy = KeywordPresenceStrategy(keywords=['test', 'response'])
        response = {'content': 'This is a test response with keywords.'}
        result = strategy.evaluate(response)
        assert result == 2

    def test_failed_evaluate(self):
        strategy = KeywordPresenceStrategy(keywords=['missing', 'keyword'])
        response = {'content': 'This is a test response.'}
        result = strategy.evaluate(response)
        assert result == 0
