import os


def get_cur_dir():
    """
    获得当前脚本的运行路径
    :return:
    """
    return os.getcwd().replace('\\', '/')


def get_desk_path():
    """
    获得当前系统的桌面路径
    :return:
    """
    home_path = os.path.expanduser('~')
    return os.path.join(home_path, 'Desktop').replace('\\', '/')


def join(path, *paths):
    """
    连接路径
    :param path:
    :param paths:
    :return:
    """
    return os.path.join(path, *paths).replace('\\', '/')


desk_path = get_desk_path()
curr_path = get_cur_dir()


def join_desk(*paths):
    return join(desk_path, *paths)


def join_curr(*paths):
    temp_path = join(curr_path, 'resources')
    return join(temp_path, *paths)
