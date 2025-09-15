import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)


def run_python_file(workding_directory: str, file_path: str, args=[]):
    base_path = os.path.abspath(workding_directory)

    full_path = os.path.abspath(os.path.join(workding_directory, file_path))
    if not full_path.startswith(base_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found'
    if not full_path.endswith(".py"):
        return f'Error "{file_path}" is not a Python file'
    command = ["python3", full_path]
    command.extend(args)
    try:
        completed = subprocess.run(command, timeout=30.0, capture_output=True)
        result_summary = f"The completed process has a STDOUT: {completed.stdout} and STDERR: {completed.stderr} attribute."
        if completed.returncode != 0:
            result_summary += f" Process exited with code {completed.returncode}"
        if not completed.stdout and not completed.stderr:
            return "No output produced"
        return result_summary
    except Exception as e:
        return f"Error: {e}"
