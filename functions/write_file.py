import os


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
