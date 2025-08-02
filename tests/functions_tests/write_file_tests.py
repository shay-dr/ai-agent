import os
from functions.write_file import write_file


if __name__ == "__main__":
    allowed_dir = os.path.abspath("calculator")
    print(f"Allowed working directory: {allowed_dir}\n")

    # Overwrites 'lorem.txt' in the 'calculator' working directory.
    # Expects: Successfully wrote to "lorem.txt" (28 characters written)
    print(f'{write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")}')

    # Overwrites 'lorem.txt' in the allowed_dir absolute directory.
    # Expects: Successfully wrote to "lorem.txt" (28 characters written)
    print(f'{write_file(allowed_dir, "lorem.txt", "wait, this isn't lorem ipsum")}')

    # Overwrites 'morelorem.txt' inside the 'pkg' subdirectory of 'calculator'.
    # Expects: Successfully wrote to "pkg/morelorem.txt" (26 characters written)
    print(f'{write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")}')

    # Overwrites 'morelorem.txt' inside the 'pkg' subdirectory of the allowed_dir absolute directory.
    # Expects: Successfully wrote to "pkg/morelorem.txt" (26 characters written)
    print(f'{write_file(allowed_dir, "pkg/morelorem.txt", "lorem ipsum dolor sit amet")}')

    # Attempts to write to '/tmp/temp.txt', which is outside the allowed directory. (Allowed directory: absolute path to 'calculator')
    # Expects: Error: Cannot write to "/tmp/temp.txt" as it is outside the permitted working directory
    print(f'{write_file("calculator", "/tmp/temp.txt", "this should not be allowed")}')

    # Attempts to write to '/tmp/temp.txt', which is outside the allowed directory while the allowed_dir is a absolute path.
    # Expects: Error: Cannot write to "/tmp/temp.txt" as it is outside the permitted working directory
    print(f'{write_file(allowed_dir, "/tmp/temp.txt", "this should not be allowed")}')

    # Attempts to traverse outside the directory using '../' in file_path.
    # Expects: Error: Cannot write to "../lorem.txt" as it is outside the permitted working directory
    print(f'{write_file("calculator", "../lorem.txt", "sneaky sneaky")}')



