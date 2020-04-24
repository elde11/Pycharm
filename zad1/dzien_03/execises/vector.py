class Vector:
    # TODO:
    # counter
    # vector[0] = 12 #__setitem__
    # hide x and y
    # or
    # use tuple/list instead of self.x self.y
    def __init__(self, frist_point, second_point):
        self._frist_point = frist_point
        self._second_point = second_point


    def lenght(self):
        return self._frist_point.distance(self._second_point)


    def __lt__(self, other_vector):
        return self.lenght() < other_vector.lenght()

point_a = Point(0,0)
point_b = Point(10,10)
point_c = Point (15,15)

vector_one = Vector(point_a,point_b)
vector_two = Vector(point_a,point_c)
print(vector_one.lenght())
print(vector_one.__lt__(vector_two))
print(vector_one >= vector_two)
print(vector_one == vector_two)