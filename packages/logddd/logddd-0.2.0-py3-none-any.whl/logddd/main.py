import inspect
import time
from os.path import basename


def log(*args):
    # 获取方法调用栈
    callFrame = inspect.currentframe().f_back
    frameInfo = inspect.getframeinfo(callFrame)
    # 文件名信息
    filename = basename(frameInfo.filename)

    code = str(frameInfo.code_context).replace(" ", '').replace('\\n', '').replace('\'', '').replace('[', '').replace(
        ']', '')
    cur_time = time.asctime()
    log_location = f'{frameInfo.filename}:{frameInfo.lineno}'
    res = f"\033[1;33m {filename}:{frameInfo.lineno}\tline:{frameInfo.lineno}\033[0m -> \033[32m{code}\033[0m : \033[1;34m {args}\033[0m {cur_time}"
    print(f'\n{log_location}\n{res}')


def le(*args):
    """
        打印日志并关闭程序
    :param args:
    :return:
    """
    log(args)
    exit(0)
