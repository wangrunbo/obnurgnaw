import threading
import gc
from consts import *
from functions import run
from exceptions.CommendError import CommendError, AttributeNotFoundError, ObjectNotExistError


class Sig(threading.Thread):
    """元"""
    name = None

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        run(self.__run)

    def __run(self):
        pass


class World(Sig):

    time = 0  # 世界时间

    def __init__(self, name):
        Sig.__init__(self, name)

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

    __mode = 'Window'
    __output = None
    __world = None

    def __init__(self):
        threading.Thread.__init__(self)

        self.__world = self.__obj('World')

    def run(self):
        while True:
            commend = input(self.__mode + '>>> ')

            units = commend.split(':')

            try:
                if len(units) == 1:
                    # 查询模式
                    units = units[0].split('@')
                    units.reverse()
                    count = len(units)
                    units = iter(units)

                    if count == 1:
                        check = self.__world
                    else:
                        check = self.__obj(next(units))

                    for attr in units:
                        if hasattr(check, attr):
                            check = getattr(check, attr)
                        else:
                            raise AttributeNotFoundError('错误！' + check.__class__.__name__ + '中不存在' + attr + '！')

                    self.__output = check

                elif len(units) == 2:
                    # 干预模式
                    self.__output = '设置成功！！'
                else:
                    raise CommendError('拒绝，指令未识别！！')
            except CommendError as e:
                self.__output = e

            self.__out()

    def __out(self):
        print(self.__output)

    def __obj(self, name):
        """
        获取目标
        :param str name: 目标name
        :return: obj
        :raise: ObjectNotExistError
        """
        for obj in gc.get_objects():
            if hasattr(obj, 'name') and type(obj.name) == str and obj.name.lower() == name.lower():
                return obj

        for obj in gc.get_objects():
            if obj.__class__.__name__.upper() == name.upper():
                return obj

        raise ObjectNotExistError(name + '不存在！')


########################################################################################################################
########################################################################################################################

obnurgnaw = World(WORLD_NAME)

obnurgnaw.start()
Window().start()


