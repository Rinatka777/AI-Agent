import os

def write_file(working_directory, file_path, content):
    actual_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    actual_working_path = os.path.abspath(working_directory)

    if os.path.commonpath([actual_file_path, actual_working_path]) != actual_working_path:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    os.makedirs(os.path.dirname(actual_file_path), exist_ok=True)

    try:
        with open(actual_file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {str(e)}"


