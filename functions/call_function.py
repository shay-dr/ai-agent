from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def call_function(function_call_part, verbose=False):
    working_directory = "./calculator"
    args = dict(function_call_part.args)
    args["working_directory"] = working_directory


    # Define and map available functions to the LLM
    function_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "write_file": write_file,
        "run_python_file": run_python_file,
    }

    # Verifies the the desired function exists before attempting to call it.
    if function_call_part.name not in function_map:
        return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"error": f"Unknown function: {function_call_part.name}"},
            )
        ],
    )
    
    func = function_map[function_call_part.name]
    result = func(**args)
    # print("DEBUG: result is", result) --troubleshooting call_function

    if verbose is True:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    
    return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_call_part.name,
            response={"result": result},
            )
        ],
    )

