import threading
import random


class Creature(threading.Thread):
    """
    生物
    """
    age = 0

    def __init__(self, age):
        threading.Thread.__init__(self)
        self.age = age
