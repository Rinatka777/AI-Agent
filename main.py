import os
import sys
from dotenv import load_dotenv
from google.genai import types
from google import genai
from functions.get_files_info import schema_get_files_info, get_files_info, schema_get_file_content, get_file_content,schema_run_python_file, run_python_file, schema_write_file, write_file

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
    ]
)

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, create a plan using function calls. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide must be relative to the working directory. You do not need to specify the working directory in your function calls — it is automatically injected for safety and sandboxing.

Use function calls when appropriate. Avoid making assumptions about file contents or execution results without reading or running them first.
"""


WORKING_DIRECTORY = "calculator"


def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config = types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,
        ),
    )

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    if response.function_calls:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")

            if function_call_part.name == "get_files_info":
                directory = function_call_part.args.get("directory")
                result = get_files_info(WORKING_DIRECTORY, directory)
                print(result)

            if function_call_part.name == "get_file_content":
                file_path = function_call_part.args.get("file_path")
                result = get_file_content(WORKING_DIRECTORY, file_path)
                print(result)

            if function_call_part.name == "run_python_file":
                file_path = function_call_part.args.get("file_path")
                result = run_python_file(WORKING_DIRECTORY, file_path)
                print(result)

            elif function_call_part.name == "write_file":
                file_path = function_call_part.args.get("file_path")
                content = function_call_part.args.get("content")
                result = write_file(WORKING_DIRECTORY, file_path, content)
                print(result)

    else:
        print("Response:")
        print(response.text)


if __name__ == "__main__":
    main()
