class Vector:
    # TODO:
    # counter
    # vector[0] = 12 #__setitem__
    # hide x and y
    # or
    # use tuple/list instead of self.x self.y
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        x_dif = self.x - other_point.x
        y_dif = self.y - other_point.y
        dist = (x_dif ** 2 + y_dif ** 2) ** 0.5
        return (dist)

    def __eq__(self, other_point):
        return (self.x == other_point.x and self.y == other_point.y)

    def __add__(self, other_point):
        new_x = self.x + other_point.x
        new_y = self.y + other_point.y
        return (new_x, new_y)

    def __str__(self):
        return f"Point {self.x},{self.y}"

    def __sub__(self, other_point):

        new_x = self.x - other_point.x
    new_y = self.y - other_point.y
    return Point(new_x, new_y)


    def __getitem__(self, index):
    if index == 0:
        return self.x
    elif index == 1:
        return self.y
    else:
        raise IndexError("No such vector index")


point_a = Point(5, 10)
point_b = Point(5, 10)
print(point_a.distance(point_b))
print(point_a == point_b)
print(point_a + point_b)
