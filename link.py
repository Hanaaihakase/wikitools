import re
from file import *

def delink(file_dir, file_name, file_type):
    # Read the file from the file path
    file_content = file_read(file_dir, file_name, file_type)
    file_path = fr"{file_dir}\{file_name}.{file_type}"

    # Delete all the <link>
    file_content = re.sub(r'<link\s.*?>', '', file_content, flags=re.DOTALL)

    # Write the file to the file path
    file_write(file_dir, file_name, file_type, file_content)

    print(fr"All <link> marks in {file_path} has been deleted!")
