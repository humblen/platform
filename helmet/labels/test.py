import os

def find_duplicate_filenames(folder1, folder2):
    # 获取第一个文件夹中的所有文件名
    filenames1 = set(os.listdir(folder1))
    # 获取第二个文件夹中的所有文件名
    filenames2 = set(os.listdir(folder2))

    # 找出重复的文件名
    duplicate_filenames = filenames1.intersection(filenames2)

    if duplicate_filenames:
        print("发现重复的文件名:")
        for filename in duplicate_filenames:
            print(filename)
    else:
        print("未发现重复的文件名。")

# 替换为实际的文件夹路径
folder1_path = "train"
folder2_path = "test"

find_duplicate_filenames(folder1_path, folder2_path)
    
