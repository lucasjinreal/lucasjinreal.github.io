import imageio
from PIL import Image
import os
import glob
import sys

# 确保提供了目录作为命令行参数
if len(sys.argv) < 2:
    print("Usage: python script.py <directory>")
    sys.exit(1)

# 获取所有以 "aa" 开头的 PNG 文件路径
imgs = sorted(glob.glob(os.path.join(sys.argv[1], "aa*.png")))

# 读取并调整第一张图像的大小，以确定所有帧的尺寸
if imgs:
    first_img = Image.open(imgs[0]).convert("RGB").resize((480, 360))
    target_size = first_img.size
else:
    print("No images found.")
    sys.exit(1)

# 创建一个列表来存储调整大小后的图像
images = []

# 遍历所有图像，调整大小并添加到列表中
for i in imgs:
    img = Image.open(i).convert("RGB")  # 确保统一颜色模式
    img = img.resize(target_size)  # 调整到目标尺寸
    images.append(img)

# 保存为 GIF 动画
try:
    imageio.mimsave("aa.gif", [img.copy() for img in images], duration=300, loop=0)
    print("GIF created successfully.")
except ValueError as e:
    print(e)
