from functions.get_files_info import get_files_info


if __name__ == "__main__":
   
   # tests directory_ls functionality
    print("Result for current directory:")
    print(f'{get_files_info("calculator", ".")}')
    '''
    Expected output:
    Result for current directory:
    - main.py: file_size=576 bytes, is_dir=False
    - tests.py: file_size=1343 bytes, is_dir=False
    - pkg: file_size=92 bytes, is_dir=True
    '''

    # tests that the function correctly lists files within a valid subdirectory
    print("Result for 'pkg' directory:")
    print(f'{get_files_info("calculator", "pkg")}')
    '''
    Expected output:
    - calculator.py: file_size=1739 bytes, is_dir=False
    - render.py: file_size=768 bytes, is_dir=False
    '''

    #tests Guardrail to ensure directory parameter is a relaitive path within the working directory
    print("Result for '/bin' directory:")
    print(f'{get_files_info("calculator", "/bin")}')
    '''
    Expected output:
        Error: Cannot list "/bin" as it is outside the permitted working directory
    '''
    #tests Guardrail to ensure directory parameter is a relaitive path within the working directory
    print("Result for '../' directory:")
    print(f'{get_files_info("calculator", "../")}')
    '''
    Expected output:
    Error: Cannot list "../" as it is outside the permitted working directory
    '''