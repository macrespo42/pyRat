import os
from config import FILE_SIZE_LIMIT
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {FILE_SIZE_LIMIT} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)


def get_file_content(workding_directory: str, file_path: str) -> str:
    base_path = os.path.abspath(workding_directory)

    full_path = os.path.abspath(os.path.join(workding_directory, file_path))
    if not full_path.startswith(base_path):
        return f'Error: Cannot read "{file_path}" as is outside the permitted working directory'
    if not os.path.isfile(full_path):
        return f"Error: File not found or is not a regular file: {file_path}"
    try:
        file_content = ""
        with open(full_path, "r") as file:
            file_content = file.read(FILE_SIZE_LIMIT)
            if len(file.read()) > len(file_content):
                file_content += (
                    f" ...File {file_path} truncated at {FILE_SIZE_LIMIT} characters"
                )
        return file_content
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    print(get_file_content("calculator", "lorem.txt"))
