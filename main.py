import os
import sys
from dotenv import load_dotenv
from google.genai import types
from google import genai

load_dotenv()

def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    user_prompt = " ".join(args)

    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]


    model = genai.GenerativeModel("gemini-2.0-flash-001")
    generate_content(model, messages, verbose)


def generate_content(model, messages, verbose):
    response = model.generate_content(messages)

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
