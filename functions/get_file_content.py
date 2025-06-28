import os

def get_file_content(working_directory, file_path):
    try:
        target_path = os.path.abspath(os.path.join(working_directory, file_path))
        working_path = os.path.abspath(working_directory)

        if os.path.commonpath([target_path, working_path]) != working_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" is not a file'
        
        MAX_CHARS = 10000
        with open(target_path, 'r', encoding='utf-8') as f:
            return f.read(MAX_CHARS)
        
    
    except Exception as e:
        return f"Error: {str(e)}"

