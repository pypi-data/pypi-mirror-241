from typing import Union, List
from pathlib import Path

import numpy as np
import pandas as pd
from AioSpider import logger

try:
    import tabula
except:
    logger.warning("未安装tabula库")
try:
    import cv2
except:
    logger.warning("未安装cv2库")
try:
    from PIL import Image
except:
    logger.warning("未安装PIL库")
try:
    from ddddocr import DdddOcr
except:
    logger.warning("未安装ddddocr库")


def extract_table_from_pdf(path: Union[str, Path], pages: Union[int, str] = 'all', encoding: str = 'utf-8'):

    if isinstance(path, Path):
        path = str(path)

    try:
        tables = tabula.read_pdf(path, pages=pages, encoding=encoding)
    except UnicodeDecodeError:
        tables = tabula.read_pdf(path, pages=pages, encoding='gbk')
    except:
        return []

    return tables


def extract_table_from_xlsx(path: Union[str, Path]):

    if isinstance(path, Path):
        path = str(path)

    try:
        df = pd.read_excel(path, engine='openpyxl')
    except (OSError, zipfile.BadZipFile) as e:
        logger.error(f"{path} 未解析到文件中的表格，原因：{e}")
        df = pd.DataFrame()

    return df


def concat(dataframes: List[pd.DataFrame], axis: int = 0):
    if not dataframes:
        return pd.DataFrame()

    df = pd.concat(dataframes, axis=0)
    df.reset_index(drop=True, inplace=True)

    return df


class ExtractImageTable:
    """
        提取图片中的表格
        @Params：
            path (Union[str, Path]): 图像文件的路径
            scale_col (int): 计算交点坐标时的列缩放因子，默认为40
            scale_row (int): 计算交点坐标时的行缩放因子，默认为20
            threshold (int): 坐标筛选的阈值，用于去除相邻相似坐标，默认为10
        @Return:
            DataFrame
    """

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.__init__(*args, **kwargs)
        return instance.detect()

    def __init__(
            self, path: Union[str, Path], scale_col: int = 40, scale_row: int = 20, threshold: int = 10
    ):
        self.image = self.read_image(path)
        self.ocr_obj = DdddOcr()
        self.scale_col = scale_col
        self.scale_row = scale_row
        self.threshold = threshold

    def detect(self):

        if self.image is None:
            return pd.DataFrame()

        binary = self.convert_image()
        x, y = self.calculate_intersection(binary)
        x_point_arr, y_point_arr = self.filter_coordinates(x, y)

        # 循环y坐标，x坐标分割表格
        data = [
            [
                self.ocr(
                    self.cut_image(
                        (x_point_arr[j], y_point_arr[i]), (x_point_arr[j + 1], y_point_arr[i + 1])
                    )
                ) for j in range(len(x_point_arr) - 1)
            ] for i in range(len(y_point_arr) - 1)
        ]

        return pd.DataFrame(data)

    def read_image(self, path):
        return np.array(Image.open(path))

    def convert_image(self):
        """将图片二值化"""
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        return cv2.adaptiveThreshold(~gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, -5)

    def calculate_intersection(self, binary):
        """计算图像表格中的交点坐标"""

        rows, cols = binary.shape

        # 识别横线和竖线
        kernel_col = cv2.getStructuringElement(cv2.MORPH_RECT, (cols // self.scale_col, 1))
        kernel_row = cv2.getStructuringElement(cv2.MORPH_RECT, (1, rows // self.scale_row))

        eroded_col = cv2.erode(binary, kernel_col, iterations=1)
        dilated_col = cv2.dilate(eroded_col, kernel_col, iterations=1)

        eroded_row = cv2.erode(binary, kernel_row, iterations=1)
        dilated_row = cv2.dilate(eroded_row, kernel_row, iterations=1)

        # 合并横竖线
        bitwise_and = cv2.bitwise_and(dilated_col, dilated_row)

        # 将焦点标识取出来
        y, x = np.where(bitwise_and > 0)

        return x, y

    def average_difference(self, arr):

        n = len(arr)
        if n < 2:
            return 0  # 如果数组中只有一个或没有元素，则差值平均值为0

        # 计算相邻元素之间的差值并计算总和
        diff_sum = sum(arr[i] - arr[i - 1] for i in range(1, n))

        # 计算平均值
        avg_diff = diff_sum / (n - 1)

        return avg_diff.round(3)

    def filter_coordinates(self, x, y):
        """筛选坐标，去除相邻的相似坐标，获得表格的边界坐标"""

        # 按升序排序坐标数组
        sorted_x = np.sort(x)
        sorted_y = np.sort(y)

        # 初始化结果数组
        x_point_arr = [sorted_x[0]]
        y_point_arr = [sorted_y[0]]

        # 遍历坐标数组，去除相邻的相似坐标
        for i in range(1, len(sorted_x)):
            if sorted_x[i] - x_point_arr[-1] > self.threshold:
                x_point_arr.append(sorted_x[i])

        for i in range(1, len(sorted_y)):
            if sorted_y[i] - y_point_arr[-1] > self.threshold:
                y_point_arr.append(sorted_y[i])

        # 往前补
        avg_x = self.average_difference(y_point_arr)
        avg_y = self.average_difference(y_point_arr)

        for i in range(1, int(x_point_arr[0] // avg_x) + 1):
            if int(x_point_arr[0] - avg_x * i) > 0:
                x_point_arr.insert(0, int(x_point_arr[0] - avg_x * i))

        for i in range(1, int(y_point_arr[0] // avg_y) + 1):
            if int(y_point_arr[0] - avg_y * i) > 0:
                y_point_arr.insert(0, int(y_point_arr[0] - avg_y * i))

        return x_point_arr, y_point_arr

    def cut_image(self, pos1, pos2):
        """切割图像，将openCV图像转换为PIL图像"""
        x1, y1 = pos1
        x2, y2 = pos2
        cell = self.image[y1: y2, x1: x2]
        return Image.fromarray(cell)

    def ocr(self, content):
        """识别"""
        return self.ocr_obj.classification(content)