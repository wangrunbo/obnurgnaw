from creatures.plants import *


class Tree(Plant):
    """
    树木
    """
    height = 0
    radius = 0
    leaves = Leaf(amount=0, color='green')
    flowers = Flower(amount=0, color='red')

    def __init__(self, age, height, radius, leaves, flowers):
        Plant.__init__(self, age)
        self.age = age
        self.height = height
        self.radius = radius
        self.leaves = leaves
        self.flowers = flowers


    def __grow(self):
        """
        成长
        :return: None
        """
        self.age += 1

        self.height += 2
        self.radius += 1

        self.leaves.summation += 10