import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_function import call_function
from functions.get_files_infos import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""


def get_available_functions():
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file,
        ]
    )
    return available_functions


def main(prompt: str, verbose=False):
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[get_available_functions()], system_instruction=system_prompt
        ),
    )
    if response.function_calls:
        for call in response.function_calls:
            print(f"Calling function: {call.name}({call.args})")
            result = call_function(call)
            if not result.parts[0].function_response.response:
                raise SystemError(
                    f"Fatal error when executing {call.name} function with {call.args} arguments"
                )
            if verbose:
                print(f"-> {result.parts[0].function_response.response}")
    else:
        print(response.text)
    if verbose:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        verbose = len(sys.argv) == 3 and sys.argv[2] == "--verbose"
        main(sys.argv[1], verbose=verbose)
    else:
        print("Please provide a prompt as script argument")
        exit(1)
