"""
面向opencv实现的图像增强
"""
import cv2
import numpy as np


__all__ = []


def bgr2hsv(bgr_img):
    hsv_img = cv2.cvtColor(bgr_img,cv2.COLOR_BGR2HSV)
    return  hsv_img


def log_transform(img,bright,contrast):
    """
    对数变换
    :param img: 输入图像
    :param c: 控制图像的亮度 参考值70
    :param v: 对比度增强因子，控制图像的对比度，v值小时对比度会更明显 参考值5
    :return: 对数变换后的图像
    """
    return np.uint8(bright * (np.log1p(img) / np.log1p(contrast)))


def image_inverse(x):
    """
    颜色翻转，输入图像为灰度图像
    :param x:
    :return:
    """
    if len(x.shape) == 2:  # 断言
        value_max = np.max(x)
        y = value_max - x
    return y


def Flip_image(img,opt):
    """
    opencv格式图片--翻转
    :param filp_code: 翻转因子：0垂直，1水平，-1水平垂直，2不翻转
    :return: flipped_image
    """
    flipped_image = cv2.flip(img, opt)
    return flipped_image


def Mean_Filter(img, kernel_size=3):
    """
    opencv图像--均值滤波
    :param kernel_size: 卷积核大小
    :param img: 传入图像
    :return: 均值滤波处理后的图像
    """
    if kernel_size % 2 == 0:
        kernel_size += 1  #判断卷积核大小是否为奇数
    w, h = img.shape[:2]
    pad_width = (kernel_size - 1) // 2
    img_pad = cv2.copyMakeBorder(img, pad_width, pad_width, pad_width, pad_width, cv2.BORDER_CONSTANT) #copyMakeBorder给图片添加边框，参数:src：原图 top, bottom, left, right：上下左右要扩展的像素数 borderType：边框类型，填充方式
    img_filter = np.zeros_like(img)  #初始化零矩阵，大小跟原图一样
    for i in range(w):
        for j in range(h):
            pixel_values = img_pad[i:i + kernel_size, j:j + kernel_size].flatten() #flatten是numpy.ndarray.flatten的一个函数，即返回一个一维数组。
            img_filter[i, j] = np.mean(pixel_values)
    return img_filter


def scale_image(img, scale_factor):
    """
    opencv格式图片--中心缩放
    :param img: 传入图像
    :param scale_factor: 缩放大小
    :return: scaled_image
    """
    height, width = img.shape[:2] #获取图像的形状信息（height， width， channels）
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)

    #计算中心位置
    center_x, center_y = width // 2, height // 2 # //是地板除 保留商的整数部分

    #建立平移矩阵，将中心点移到图像的中心
    translation_matrix = np.array([[1, 0, center_x - new_width // 2],
                                   [0, 1, center_y - new_height // 2]], dtype=np.float32)

    #使用仿射变换进行缩放
    scaled_image = cv2.warpAffine(img, translation_matrix, (new_width, new_height))
    return scaled_image


def fill(img):
    """
    opencv格式图片--灰度填充
    :param x: 图像转换
    :return: 处理后图像
    """
    cv2.imshow('input', img)
    h, w, ch = img.shape  # 图像的高，宽，通道数
    color = [128,128,128]  # 新颜色，bgr
    for i in range(h):
        for j in range(w):
            if img[i, j, 0] >= 100:  # 如果b通道值大于128，说明找到了目标背景色，那么就给bgr三通道赋新值
                img[i, j, 0] = color[0]
                img[i, j, 1] = color[1]
                img[i, j, 2] = color[2]
    return img


def medianBlur(img, kernel_size):
    """
    opencv格式图片--灰度反转
    :param img: 传入图像
    :param kernel_size: 卷积核
    :return: 中值滤波处理后的图像
    """
    h, w = img.shape[:2]
    half = kernel_size // 2
    start = half
    end = h - half - 1
    dst = np.zeros((h, w), dtype=np.uint8)
    for y in range(start, end):
        for x in range(start, end):
            a = []
            for i in range(y - half, y + half + 1):
                for j in range(x - half, x + half + 1):
                    a.append(img[i][j])
            # 取中间值
            a = np.sort(a, axis=None)
            if len(a) % 2 == 1:
                medValue = a[len(a) // 2]
            else:
                medValue = int((a[len(a) // 2] + a[len(a) // 2 + 1]) / 2)
            dst[y][x] = medValue
    return dst


def hist_equal(img, z_max=255):
    """
    opencv格式图片--直方图均衡
    :param img: 传入图像
    :param z_max: 图像像素的最大取值
    :return: 中值滤波处理后的图像
    """
    h, w = img.shape
    s = h * w * 1.  #s是像素的总数
    out = img.copy()  #创建输入与图像的副本

    sum_h = 0.   #累积像素的数量

    for i in range(1, 255):
        i1 = np.where(img == i)     #查找图像中像素值为i的像素的位置
        sum_h += len(img[i1])       #计算像素值小于或等于i的像素的总数
        z_prime = z_max / s * sum_h     #直方图均衡化的算法公式
        out[i1] = z_prime       #根据sum_h累积像素总数来计算新的像素值

    out = out.astype(np.uint8)     #输出图像并将图像的数据类型转变为uint8确保图像像素的值在0-255之间

    return out