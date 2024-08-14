from user_interface.cli import CLI
from user_interface.command import SendPromptCommand, Invoker
from api_connection.api_gemini import GeminiFactory
from api_connection.api_chatgpt import ChatGPTFactory
from response_processing.strategies import WordCountStrategy, KeywordPresenceStrategy
from utils.result_print import print_results
from results_presentation.observer import ResponseObserver, Subject

def main():
    # Instantiate the CLI
    cli = CLI()
    cli.load_environment()
    cli.load_config()
    cli.parse_arguments()

    # API keys and parameters
    gemini_api_key, chatgpt_api_key = cli.get_api_keys()
    prompt = cli.get_prompt()
    strategy_choice = cli.get_strategy()
    keywords = cli.get_keywords()

    # Create factories for the LLMs
    gemini_factory = GeminiFactory(gemini_api_key)
    chatgpt_factory = ChatGPTFactory(chatgpt_api_key)

    # Define the prompt
    prompt = [{"role": "user", "content": prompt}]

    # Choose the evaluation strategy based on the arguments
    if strategy_choice == "word_count":
        strategy = WordCountStrategy()
    else:
        strategy = KeywordPresenceStrategy(keywords=keywords)

    # Create the commands to send prompts and evaluate responses
    gemini_command = SendPromptCommand("Gemini", gemini_factory, prompt, strategy)
    chatgpt_command = SendPromptCommand("ChatGPT", chatgpt_factory, prompt, strategy)

    # Create the invoker and add commands
    invoker = Invoker()
    invoker.add_command(gemini_command)
    invoker.add_command(chatgpt_command)

    # Create and attach an observer
    observer = ResponseObserver()
    subject = Subject()
    subject.attach(observer)

    # Execute the commands
    results = invoker.execute_commands()

    subject.notify("Response processing completed.")

    print_results(results)

if __name__ == "__main__":
    main()