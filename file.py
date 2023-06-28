import os

def dir_make(dir_path):
    # 确保目录存在
    os.makedirs(dir_path, exist_ok=True)

def file_save(save_title, save_type, save_content, save_path):
    # 确保保存路径存在
    dir_make(save_path)

    # 将内容保存到本地文件
    file_path = os.path.join(save_path, f"{os.path.basename(save_title)}.{save_type}")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(save_content)

    print(f"{file_path} has been saved!")