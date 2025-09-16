from google.genai import types
from functions.get_files_infos import get_files_infos
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file
from config import ROOT


def call_function(function_call_part: types.FunctionCall, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    functions_dict = {
        get_files_infos.__name__: get_files_infos,
        get_file_content.__name__: get_file_content,
        run_python_file.__name__: run_python_file,
        write_file.__name__: write_file,
    }
    function_name = function_call_part.name or ""
    args = function_call_part.args or {}
    fx = functions_dict.get(function_name)
    if not fx:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    function_result = fx(ROOT, **args)
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
