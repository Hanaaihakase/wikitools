import os

def file_write(file_dir, file_name, file_type, file_content):
    # Ensure the file path exists
    os.makedirs(file_dir, exist_ok=True)

    # Create the file path
    file_path = fr"{file_dir}\{file_name}.{file_type}"

    # Write the file content to the file path
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(file_content)

    print(f"{file_path} has been written!")

def file_read(file_dir, file_name, file_type):
    # Create the file path
    file_path = fr"{file_dir}\{file_name}.{file_type}"

    # Read the file content from the file path
    with open(file_path, "r", encoding="utf-8") as file:
        file_content = file.read()

    print(f"{file_path} has been read!")

    # Return the file content
    return file_content
