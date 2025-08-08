import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    # This is a dangerous function! Either enhance the security and safeguards or remove before using outside of this project!
    
     # IMPORTANT Guardrail to ensure file_pat parameter is a relaitive path within the working directory
    
    abs_working_dir = os.path.abspath(working_directory)
    relative_path = os.path.join(working_directory, file_path) #combined paths
    abs_path = os.path.abspath(relative_path) # absolute path
    cmd = ["python", abs_path] + args

    if not abs_path.startswith(abs_working_dir):
        return (f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')

    # Guardrail to ensure file_path exists
    if not os.path.exists(abs_path):
        return (f'Error: File "{file_path}" not found.')
    
    # Verifies the file ends with .py
    if not file_path.endswith(".py"):
        return (f'Error: "{file_path}" is not a Python file.')
    
   
    # Run script
    try:
        script_exec = subprocess.run(cmd, timeout=30, capture_output=True, cwd=abs_working_dir )
        
        # Capture script results
        result_stdout = str(script_exec.stdout.decode(encoding='UTF-8', errors='strict'))
        result_stderr = str(script_exec.stderr.decode(encoding='UTF-8', errors='strict'))
        output = (f'STDOUT:{result_stdout}\nSTDERR:{result_stderr}')

        if not result_stdout.strip() and not result_stderr.strip():
            return "No output produced."
        if script_exec.returncode != 0:
            return (f'{output}\nProcess exited with code {script_exec.returncode}')
        
        return (output)
    
    except Exception as e:
        return (f"Error: executing Python file: {e}")



