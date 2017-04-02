import time
from consts import *


def run(action, *args):
    """
    执行
    :param action: 每１基础时间内执行的操作
    :return: 
    """
    overtime = 0  # 动作超出基础时间秒数

    while True:
        time_start = time.time()

        # TODO 定格状态

        action(*args)

        time_end = time.time()

        if time_end - time_start < BASE_TIME - overtime:
            time.sleep(BASE_TIME - (time_end - time_start) - overtime)
            overtime = 0
        else:
            overtime = (time_end - time_start) - (BASE_TIME - overtime)


if __name__ == '__main__':
    put = input('putin1')
    put2 = input('putin2')
    print(put)
    print(put2)
