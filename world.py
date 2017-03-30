import time
import threading
from consts import *


class World(threading.Thread):

    time = 0

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            self.elapse()
            time.sleep(BASE_TIME)

    def elapse(self):
        """
        时间流逝
        :return: None
        """
        self.time += 1


if __name__ == '__main__':
    print('hello')
