import math

class Shape:
    def __init__(self):
        pass
    def area(self):
        raise NotImplementedError
    def circumference(self):
        raise NotImplementedError
# Stworzyć klase Shape z metodami kostruktor, area, circumference )
# utworzyc klasy pochodne
# rectange, square, circle
# i odpowiednio je zaimplmentować
class Rectangle(Shape):
    def __init__(self, x,y):
        super().__init__()
        self.x = x
        self.y = y

    def area(self):
        super().area()
        return self.x * self.y

    def circumference(self):
        super().area()
        return 2 * (self.x * self.y)


class Square(Rectangle) :
    def __init__(self, x):
        super().__init__(x,x)


class Circle(Shape)
    pi = math.pi
    def __init__(self,r):
        super().__init__()
        self.r =r
    def area(self):
        return self.pi * self.r ** 2


rec = Rectangle(10,20)
square = Square(10)
circle = Circle (4)

print(rec.circumference())
print(rec.area())

print(circle.area())