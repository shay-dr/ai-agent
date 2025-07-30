from functions.get_file_content import get_file_content


if __name__ == "__main__":

    # tests truncation with lorem.txt (should be > 10,000 chars) 
    result = get_file_content("calculator", "lorem.txt")
    print("Testing lorem.txt truncation:")
    print(f"Length of result: {len(result)}")
    print("Does it contain truncation message?", "[...File" in result)
    print("Last 100 characters:", result[-100:])

   

    # Shows the complete file content for a file within this directory.
    print(f'{get_file_content("calculator", "main.py")}')

    # Shows the complete file content for a file in a different directory.
    print(f'{get_file_content("calculator", "pkg/calculator.py")}')

    # This should return an error string.
    print(f'{get_file_content("calculator", "/bin/cat")}')

    # This should return an error string.
    print(f'{get_file_content("calculator", "pkg/does_not_exist.py")}') 