from creatures import Creature


class Plant(Creature):
    """
    植物
    """
    pass


class Leaf:
    """
    叶子
    """
    amount = 0
    color = 'green'

    def __init__(self, amount, color):
        self.amount = amount
        self.color = color

    def grow(self, summation):
        self.amount += summation

    def wither(self, summation):
        self.amount -= summation


class Flower:
    """
    花朵
    """
    amount = 0
    color = 'red'

    def __init__(self, amount, color):
        self.amount = amount
        self.color = color

    def grow(self, summation):
        self.amount += summation

    def wither(self, summation):
        self.amount -= summation
