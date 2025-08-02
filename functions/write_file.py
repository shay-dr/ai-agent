import os

def write_file(working_directory, file_path, content):
        
    # IMPORTANT Guardrail to ensure file_pat parameter is a relaitive path within the working directory
    
    abs_working_dir = os.path.abspath(working_directory)
    relative_path = os.path.join(working_directory, file_path) #combined paths
    abs_path = os.path.abspath(relative_path) # absolute path

    if not abs_path.startswith(abs_working_dir):
        return (f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
    
    # Writes to the file and ensures file path exists or will create the parent folders(s) if it doesn't.
    try:
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
    
        with open(abs_path, "w") as f:
            f.write(content)
            return (f'Successfully wrote to "{file_path}" ({len(content)} characters written)')

    except Exception as e:
        return f"Error: An unexpected error occurred: {e}"

    