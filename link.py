import os
import re

def delink(filename, file_path):
    # 将文件路径和文件名组合成完整的路径
    file_path = os.path.join(file_path, filename)

    # 打开文件并读取内容
    with open(file_path, "r") as f:
        content = f.read()

    # 删除所有的<link>标记
    content = re.sub(r'<link\s.*?>', '', content, flags=re.DOTALL)

    # 将修改后的内容写回文件
    with open(file_path, "w") as f:
        f.write(content)

    print(f"All <link> marks in {file_path} has been deleted!")
