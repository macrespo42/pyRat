import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)


def get_files_infos(workding_directory: str, directory: str = ".") -> str:
    base_path = os.path.abspath(workding_directory)

    full_path = os.path.abspath(os.path.join(workding_directory, directory))

    if not full_path.startswith(base_path):
        return f'Error: Cannot list "{directory}" as is outside the permitted working directory'

    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    files = os.listdir(full_path)
    files_infos = []
    for file in files:
        try:
            full_file_path = os.path.join(full_path, file)
            files_infos.append(
                f"- {file}: file_size={os.path.getsize(full_file_path)} bytes, is_dir={os.path.isdir(full_file_path)}"
            )
        except Exception as e:
            print(f"Error: {e}")
    return "\n".join(files_infos)
