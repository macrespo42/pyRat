import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)


def write_file(workding_directory: str, file_path: str, content: str):
    base_path = os.path.abspath(workding_directory)

    full_path = os.path.abspath(os.path.join(workding_directory, file_path))
    if not full_path.startswith(base_path):
        return f'Error: Cannot write "{file_path}" as is outside the permitted working directory'
    try:
        with open(full_path, "w") as f:
            f.write(content)
            return (
                f"Successfully wrote to {file_path} {len(content)} characters written"
            )
    except Exception as e:
        return f"Error: {e}"
