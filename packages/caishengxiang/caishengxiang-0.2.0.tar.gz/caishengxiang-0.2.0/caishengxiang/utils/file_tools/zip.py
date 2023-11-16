# -*-coding:utf-8-*-
import os
import zipfile
from caishengxiang.libs.zipstream import ZipStream


def get_zip_stream(dirpath, chunksize=1024 * 10):
    """
    根据实际目录路径 生成流下载对象
    """
    files = []
    parent_dir = os.path.dirname(dirpath)  # 压缩文件夹的父目录
    for path, dirnames, filenames in os.walk(dirpath):  # 遍历所有子目录
        # 去掉目标根路径，只对目标文件夹下边的文件及文件夹进行压缩
        z_dir_path = path.replace(parent_dir, '')  # 去掉父目录 获取相对目录
        for filename in filenames:
            file_path = os.path.join(path, filename)  # 文件在外面的实际路径
            z_file_path = os.path.join(z_dir_path, filename)  # 在zip内的相对路径
            files.append({'file': file_path, 'name': z_file_path})
    zs = ZipStream(files, chunksize=chunksize)
    return zs


def zip_dir(dirpath, out_path):
    """
    压缩指定文件夹 到指定路径.zip
    :param dirpath: 文件夹路径 dirpath : '/home/xiang/workproject/jpt_filesystem/static/log'
    :param out_path: 导出路径 '/home/xiang/workproject/jpt_filesystem/tests/log.zip'
    :return: 无
    """
    _diranme = os.path.dirname(dirpath)
    dir_dir_path = os.path.dirname(dirpath)  # 压缩文件夹的父目录

    zip = zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):  # 遍历所有子目录
        # 去掉目标根路径，只对目标文件夹下边的文件及文件夹进行压缩
        z_dir_path = path.replace(dir_dir_path, '')  # 去掉父目录 获取相对目录
        for filename in filenames:
            file_path = os.path.join(path, filename)  # 文件在外面的实际路径
            z_file_path = os.path.join(z_dir_path, filename)  # 在zip内的相对路径
            zip.write(file_path, z_file_path)
    zip.close()
    return out_path


def zip_dir_bytes(dirpath, zip_bytes_iO):
    """
    压缩指定文件夹 到内存
    :param dirpath:实际文件夹路径 dirpath : '/home/xiang/workproject/jpt_filesystem/static/log'
    :param zip_bytes_iO: BytesIO  例子  memory_file = BytesIO()
    :return: BytesIO
    """
    _diranme = os.path.dirname(dirpath)
    dir_dir_path = os.path.dirname(dirpath)  # 压缩文件夹的父目录

    zip = zipfile.ZipFile(zip_bytes_iO, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):  # 遍历所有子目录
        # 去掉目标根路径，只对目标文件夹下边的文件及文件夹进行压缩
        z_dir_path = path.replace(dir_dir_path, '')  # 去掉父目录 获取相对目录
        for filename in filenames:
            file_path = os.path.join(path, filename)  # 文件在外面的实际路径
            z_file_path = os.path.join(z_dir_path, filename)  # 在zip内的相对路径
            with open(file_path, 'rb') as fp:
                content = fp.read()
                print(z_file_path)
                zip.writestr(z_file_path, content)
    zip.close()
    return zip_bytes_iO