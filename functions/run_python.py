import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    actual_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    actual_working_path = os.path.abspath(working_directory)

    if os.path.commonpath([actual_file_path, actual_working_path]) != actual_working_path:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(actual_file_path):
        return f'Error: File "{file_path}" not found.'

    if not actual_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(
            ["python", actual_file_path],
            cwd=actual_working_path,
            capture_output=True,
            text=True,
            timeout=30
        )

        output_lines = []

        if result.stdout:
            output_lines.append("STDOUT:\n" + result.stdout)
        if result.stderr:
            output_lines.append("STDERR:\n" + result.stderr)
        if result.returncode != 0:
            output_lines.append(f"Process exited with code {result.returncode}")
        if not result.stdout and not result.stderr:
            output_lines.append("No output produced.")

        return "\n".join(output_lines)

    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file inside the working directory and returns its stdout and stderr.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)