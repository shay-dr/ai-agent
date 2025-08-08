import os
from google.genai import types


def get_files_info(working_directory, directory="."):

    # IMPORTANT Guardrail to ensure directory parameter is a relaitive path within the working directory
    
    abs_working_dir = os.path.abspath(working_directory)
    relative_path = os.path.join(working_directory, directory) #combined paths
    abs_path = os.path.abspath(relative_path) # absolute path

    if not abs_path.startswith(abs_working_dir):
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    
    #  Guardrail to ensure directory parameter is directory
    if not os.path.isdir(abs_path):
        return (f'Error: "{directory}" is not a directory')
    
    # Obtain metadata for items in a directory
    try:

        directory_ls = ""

        for item in os.listdir(abs_path):
            item_name = item
            if item_name != "__pycache__":
                item_size = os.path.getsize(os.path.join(abs_path, item))
                item_if_dir = os.path.isdir(os.path.join(abs_path, item))
                directory_ls += f"- {item_name}: file_size={str(item_size)} bytes, is_dir={str(item_if_dir)} \n"

        return directory_ls
    
    except Exception as e:
        return f"Error: An unexpected error occurred: {e}"
    

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
