import shutil
import zipfile
from typing import Union
from pathlib import Path

from AioSpider import logger


def mkdir(path: Union[Path, str], auto: bool = True):
    """
    创建目录
    Args:
        path: 文件夹路径
        auto: 自动判断 path 参数是文件还是文件夹子，默认为 True。当 auto 为 True 时，会自动判断 path 路径参数是否有文件
            后缀（如：.txt、.csv等），如果有则创建父级文件夹，如果没有则创建当前路径文件夹；当 auto 为 False 时，
            会已当前路径作为文件夹创建
    """

    path = Path(path) if isinstance(path, str) else path

    if path.exists():
        return

    target_path = path.parent if auto and path.suffix else path
    target_path.mkdir(parents=True, exist_ok=True)


def decompress_zip(zip_path: Union[str, Path], extract_folder: Union[str, Path], delete=True):
    """
    解压zip文件
    Args:
        zip_path: 要解压的ZIP文件路径
        extract_folder: 解压后的目标文件夹
        delete: 解压成功后删除该压缩文件
    """

    try:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            zf.extractall(extract_folder)
        if delete:
            delete_files(zip_path)
    except Exception as e:
        logger.warning(f'{zip_path} 文件解压失败！原因：{e}')


def move(source_folder, destination_folder):
    """
    移动文件夹
    Args:
        source_folder: 要剪切的源文件夹路径
        destination_folder: 目标文件夹路径
    """

    try:
        shutil.move(source_folder, destination_folder)
    except FileExistsError:
        logger.warning(f'{destination_folder} 文件（夹）已存在')
    except FileNotFoundError:
        logger.warning(f'{source_folder} 文件（夹）不存在')


def rename(old_name, new_name):
    """
    移动文件夹
    Args:
        old_name: 要重命名的文件夹路径
        new_name: 新的文件夹名
    """

    try:
        os.rename(old_name, new_name)
    except FileExistsError:
        logger.warning(f'{new_name} 文件（夹）已存在')
    except FileNotFoundError:
        logger.warning(f'{old_name} 文件（夹）不存在')


def delete_files(path: Path):
    """
    删除文件（夹）
    Args:
        path: 文件（夹）路径
    """

    try:
        if path.is_dir():
            shutil.rmtree(path)
        else:
            os.remove(path)
    except FileNotFoundError:
        logger.warning(f'{path} 文件（夹）不存在')

