def get_files_info(working_directory, directory=None):
    if directory not in working_directory:
        return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    if not directory:
        return f'Error: "{directory}" is not a directory'
    
    directory_content = []
    for file in range(directory):
        directory_content.append(file)
        print (directory_content)


