from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0


class Rectangle(Shape):
    type = "Rectangle"
    side = 4

    def __init__(self):
        self.length = 6
        self.breath = 7

    def printarea(self):
        return self.breath * self.length


ret1 = Rectangle()
print(ret1.printarea())
