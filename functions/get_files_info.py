import os

def get_files_info(working_directory, directory=None):
    try:
        if directory is None:
            directory = working_directory
        else:
            directory = os.path.join(working_directory, directory)

        certain_directory = os.path.abspath(directory)
        certain_working_directory = os.path.abspath(working_directory)

        if not os.path.isdir(certain_directory):
            return f'Error: "{directory}" is not a directory'

        # Guardrail: directory must be within working_directory
        is_inside = os.path.commonpath([certain_directory, certain_working_directory]) == certain_working_directory
        if not is_inside:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        file_descriptions = []
        for item in os.listdir(certain_directory):
            full_path = os.path.join(certain_directory, item)
            try:
                size = os.path.getsize(full_path)
                is_dir = os.path.isdir(full_path)
                file_descriptions.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")
            except Exception as e:
                return f"Error: {str(e)}"

        return "\n".join(file_descriptions)

    except Exception as e:
        return f"Error: {str(e)}"
