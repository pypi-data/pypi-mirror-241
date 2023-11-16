# -*-coding:utf-8-*-
import os
import sys
import subprocess
import re
import platform
import ctypes


def is_writable(path):
    """
    是否可写
    :param path：实际地址
    :return:
    """
    return os.access(path, os.W_OK)


def is_readable(path):
    """
    是否可读
    :param path: 实际地址
    :return:
    """
    return os.access(path, os.R_OK)


def is_executable(path):
    """
    是否可执行
    :param path: 实际地址
    :return:
    """
    return os.access(path, os.X_OK)

def get_path_size_by_linux(path: str):
    """
    利用 linux 原生命令 查看文件(夹)大小
    @param path:
    @return: @int size 字节
    """

    def du_sb():
        context = None
        size = None
        cmds = ['du', '-sb', path]
        p = subprocess.Popen(cmds, stdout=subprocess.PIPE)
        out, err = p.communicate()
        for line in out.splitlines():
            context = line.decode()

        if context:
            pattern = re.compile(r'^(\d+)')
            searchObj = pattern.search(context)
            size_str = searchObj.group(1)
            size = int(size_str)
        return size

    def du_sk():
        context = None
        size = None
        cmds = ['du', '-sk', path]
        p = subprocess.Popen(cmds, stdout=subprocess.PIPE)
        out, err = p.communicate()
        for line in out.splitlines():
            context = line.decode()

        if context:
            pattern = re.compile(r'^(\d+)')
            searchObj = pattern.search(context)
            size_str = searchObj.group(1)
            size = int(size_str)
        return size * 1024  # kb转b

    size = du_sb()
    if size is None:
        size = du_sk()
    return size


def get_path_size(path):
    """
    根据路径获取 文件/文件夹的大小
    :param path:
    :return: dir_size 字节
    """
    if os.path.isfile(path):
        return os.path.getsize(path)
    if 'linux' in sys.platform:  # linux原生命令性能更好
        _size = get_path_size_by_linux(path)
        if _size:
            return _size
    dir_size = 0
    for _path, dirnames, filenames in os.walk(path):  # 遍历所有子目录
        for filename in filenames:
            file_path = os.path.join(_path, filename)
            try:
                size = os.path.getsize(file_path)
            except:
                size = 0
            dir_size += size
    return dir_size


def get_suffix(file_name: str) -> str:
    """获取文件后缀"""
    suffix = ''
    split = file_name.split(".")
    if len(split) > 1:
        suffix = split[-1]
    return suffix


def check_file_too_large(path, max_size):
    """
    检查文件（夹）大小
    :param path:
    :param max_size:
    :return:
    """
    if not os.path.exists(path):
        return False
    if os.path.isfile(path):
        if os.path.getsize(path) > max_size:
            return True
    size = 0
    for path, dirnames, filenames in os.walk(path):
        # 递归查询文件大小
        for f in filenames:
            _path = os.path.join(path, f)
            try:
                _size = os.path.getsize(_path)
            except:
                _size = 0
            size += _size
            print(size)
            if size > max_size:
                return True


def check_file_too_many(path, max_num):
    """检查文件数量 （非常节约性能）"""
    if not os.path.exists(path):
        return False
    if os.path.isfile(path):
        return False
    num = 0
    for path, dirnames, filenames in os.walk(path):
        num += len(filenames)
        if num > max_num:
            return True



def get_free_space_mb(folder):
    """
    获取当前目录所在磁盘 剩余空间
    :param folder: 磁盘路径 例如 D:\\
    :return: 剩余空间 单位 G
    """
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value / 1024
    else:
        st = os.statvfs(folder)
        return st.f_bavail * st.f_frsize  # 非超级用户可获得的块数×分栈大小==磁盘剩余空间


def get_blocks_space_mb(folder):
    """获取当前目录所在磁盘 全部空间"""
    st = os.statvfs(folder)
    return st.f_blocks * st.f_frsize


def get_pvc_info(folder):
    """
    当前目录所在磁盘信息
    :param folder:
    :return: (剩余空间率, 剩余空间, 总空间)
    """
    free_size = get_free_space_mb(folder)  # 剩余空间
    total_size = get_blocks_space_mb(folder)
    free_space_rate = free_size / total_size
    return {'free_space_rate': free_space_rate, 'free_size': free_size, 'total_size': total_size}