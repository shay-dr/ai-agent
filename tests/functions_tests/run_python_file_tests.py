import os
from functions.run_python import run_python_file

if __name__ == "__main__":
    allowed_dir = os.path.abspath("calculator")
    print(f"Allowed working directory: {allowed_dir}\n")

    # Prints calculator's instructions
    # Expects:
    '''
    STDOUT:Calculator App
    Usage: python main.py "<expression>"
    Example: python main.py "3 + 5"
    '''
    print(f'{run_python_file("calculator", "main.py")}')

    # Runs calculator
    # Expects: 
    '''
    STDERR:
    STDOUT:┌─────────┐
    │  3 + 5  │
    │         │
    │  =      │
    │         │
    │  8      │
    └─────────┘
    '''
    print(f'{run_python_file("calculator", "main.py", ["3 + 5"])}')
    
    # Runs test.py file within calculator directory
    # Expects:
    '''
    STDERR:
    STDOUT:
    STDERR:.........
    ----------------------------------------------------------------------
    Ran 9 tests in 0.000s

    OK
    '''
    print(f'{run_python_file("calculator", "tests.py")}')  

    # Tests if file is within the hardcoded working directory
    # Expects: Error: Cannot execute "../main.py" as it is outside the permitted working directory
    print(f'{run_python_file("calculator", "../main.py")}')


    # Tests if file is within the referenced absolute path
    # Expects: Error: Cannot execute "../main.py" as it is outside the permitted working directory
    print(f'{run_python_file(allowed_dir, "../main.py")}')

    # Tests if the provided script can not be found.
    # Expects: Error: File "nonexistent.py" not found.
    print(f'{run_python_file("calculator", "nonexistent.py", ["3 + 5"])}')