import textwrap

def print_results(results):
    width = 80

    print("=" * width)
    print("{:<20} {:<15} {:<50}".format("LLM API", "Score", "Prompt"))
    print("=" * width)

    for result in results:
        api_name = result['api_name']
        prompt = result['response']['prompt']
        response_content = result['response']['content']
        score = result['score']

        print("{:<20} {:<15} {:<50}".format(api_name, f"{score:.1f}", prompt))
        print("-" * width)
        print("Response:")
        print(textwrap.fill(response_content, width=width))
        print("-" * width)

    print("=" * width)