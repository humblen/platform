import os
import random
import shutil

# 定义图片和 txt 文件的原始文件夹路径
image_folder = 'data/images'
txt_folder = 'data/labels'

# 定义划分后的文件夹路径
train_image_folder = 'images/train'
train_txt_folder = 'labels/train'
val_image_folder = 'images/val'
val_txt_folder = 'labels/val'
test_image_folder = 'images/test'
test_txt_folder = 'labels/test'

# 创建划分后的文件夹
for folder in [train_image_folder, train_txt_folder, val_image_folder, val_txt_folder, test_image_folder,
               test_txt_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# 获取所有有对应 txt 文件的图片文件名（不包含扩展名）
txt_files = [os.path.splitext(file)[0] for file in os.listdir(txt_folder) if file.endswith('.txt')]
valid_image_files = [file for file in os.listdir(image_folder) if
                     os.path.splitext(file)[0] in txt_files and file.endswith('.jpg')]

# 打乱文件名列表
random.shuffle(valid_image_files)

# 计算划分的索引
total = len(valid_image_files)
train_index = int(total * 0.7)
val_index = int(total * 0.9)

# 用于记录已处理的文件名
processed_files = set()

# 划分文件
for i, file in enumerate(valid_image_files):
    file_name = os.path.splitext(file)[0]
    image_path = os.path.join(image_folder, file)
    txt_path = os.path.join(txt_folder, f'{file_name}.txt')

    # 检查文件是否已处理
    if file_name in processed_files:
        continue

    if i < train_index:
        shutil.copy(image_path, os.path.join(train_image_folder, file))
        shutil.copy(txt_path, os.path.join(train_txt_folder, f'{file_name}.txt'))
    elif i < val_index:
        shutil.copy(image_path, os.path.join(val_image_folder, file))
        shutil.copy(txt_path, os.path.join(val_txt_folder, f'{file_name}.txt'))
    else:
        shutil.copy(image_path, os.path.join(test_image_folder, file))
        shutil.copy(txt_path, os.path.join(test_txt_folder, f'{file_name}.txt'))

    # 标记文件为已处理
    processed_files.add(file_name)

print("文件划分完成。")

