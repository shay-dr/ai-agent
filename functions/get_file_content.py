import os
from . import functions_config
from google.genai import types


def get_file_content(working_directory, file_path):
    
    
    # IMPORTANT Guardrail to ensure file_pat parameter is a relaitive path within the working directory
    
    abs_working_dir = os.path.abspath(working_directory)
    relative_path = os.path.join(working_directory, file_path) #combined paths
    abs_path = os.path.abspath(relative_path) # absolute path

    if not abs_path.startswith(abs_working_dir):
        return (f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    
    #  Guardrail to ensure file_path parameter is a file
    if not os.path.isfile(abs_path):
        return (f'Error: File not found or is not a regular file: "{file_path}"')
    
    
    # Read the file and return its contents as a string, also truncate the file if it's over {MAX_FILE_CHARS} characters
    try:

        with open(abs_path, "r") as f:
            file_content_string = f.read(functions_config.MAX_FILE_CHARS)
            next_char = f.read(1)
            if next_char:
                return (f'{file_content_string}[...File "{file_path}" truncated at {functions_config.MAX_FILE_CHARS} characters]')
            return (file_content_string)
    
    except Exception as e:
        return f"Error: An unexpected error occurred: {e}"
    

    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads the file and returns its contents as a string, also truncate the file if it's over {functions_config.MAX_FILE_CHARS} characters.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory.",
            ),
        },
    ),
)
