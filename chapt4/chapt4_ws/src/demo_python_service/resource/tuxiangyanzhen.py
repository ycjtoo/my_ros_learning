import cv2
import numpy as np

# 1. 验证矩阵形状 (H, W, C)
img = cv2.imread('default.jpg') # 找张你自己的照片
print("图像形状:", img.shape) # 输出类似 (1080, 1920, 3)，分别对应 高、宽、通道数

# 2. 验证坐标系 (左上角是0,0)
# 获取最左上角那个像素的值
print("左上角像素值 (B,G,R):", img[0, 0]) 
# 注意：代码里取值是 img[y, x]，即先写行（高度），再写列（宽度）

# 3. 验证 BGR 通道分离
b, g, r = cv2.split(img)
print("蓝色通道:", b.shape) 

# 注意 img[y, x]，行是高度，列是宽度
print("中间点像素值:", img[569, 910]) 

# 将 BGR 转换为 HSV (OpenCV 里的色域转换)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print("HSV图像的形状:", img_hsv.shape)
print("中间点的 HSV 值:", img_hsv[569, 910])
# 解释：H(色相)通常是0-180，S(饱和度)和V(明度)是0-255