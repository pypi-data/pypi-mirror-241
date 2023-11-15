import os


# 反斜杠转斜杠
def backslash2slash(path):
    return path.replace("\\", "/")


# 处理输出路径（若不存在则创建文件夹）
def make_output_dirs(output_path):
    dir_path, file_name = os.path.split(output_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


# 获取文件格式
def get_fmt(path):
    return path.split(".")[-1].lower()
