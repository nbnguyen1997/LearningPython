class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add_point(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def add_tuple(self, tupl):
        element_x, element_y = tupl
        return Point(self.x + element_x, self.y + element_y)

    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        else:
            return self.add_tuple(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return "(%d,%d)" % (self.x, self.y)


point_1 = Point(3, 4)
point_2 = Point(1, 2)
# print(point_1)
tu = ((5, 7))
print(point_1 + tu)
print(tu + point_1)
print(point_2 + point_1)
print(point_1 + point_2)
