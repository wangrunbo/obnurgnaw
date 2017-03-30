import threading
import re
import gc
from functions import *


class World(threading.Thread):

    time = 0  # 世界时间
    name = None

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        run(self.__run)

    def __elapse(self):
        """
        时间流逝
        :return: None
        """
        self.time += 1

    def __run(self):
        self.__elapse()


class Window(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            commend = input('Window>>> ')

            # keys = re.match(r'What ((is)|(are)) the (.+)( and (.+))*( of (.+))?', commend, re.I)
            keys = re.match(r'What ((is)|(are)) the (.+)', commend, re.I)  # What is the *****
            keys = re.match(r'(.+) of (.+)', keys.group(4), re.I)  # ***** of *****

            info = keys.group(1)

            for obj in gc.get_objects():
                if isinstance(obj, World):
                    print(getattr(obj, info, '拒绝，指令未识别！！'))

########################################################################################################################
########################################################################################################################

obnurgnaw = World(WORLD_NAME)

obnurgnaw.start()
Window().start()
