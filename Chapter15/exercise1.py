import math
import copy


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print_point(self):
        print("( %.2f, %.2f)" % (self.x, self.y))


class Rectangle:
    def __init__(self, width=1, height=1, cornor=Point()):
        self.width = width
        self.height = height
        self.cornor = cornor


class Circle:
    def __init__(self, center=Point(), radius=1):
        self.center = center
        self.radius = radius


def point_in_circle(circle, point):
    dis = distance(circle.center, point)

    if dis <= circle.radius:
        return True

    return False


def distance(point_1, point_2):
    return math.sqrt(
        math.pow(point_1.x - point_2.x, 2) + math.pow(point_1.y - point_2.y, 2)
    )


def rect_in_circle(circle, rectangle):
    point = copy.copy(rectangle.cornor)
    width = rectangle.width
    height = rectangle.height
    if not point_in_circle(circle, point):
        return False
    if not point_in_circle(circle, Point(point.x, point.y + height)):
        return False
    if not point_in_circle(circle, Point(point.x + width, point.y)):
        return False
    if not point_in_circle(circle, Point(point.x + width, point.y + height)):
        return False

    return True


cir = Circle(Point(150, 100), 75)

# print(distance(Point(3, 0), Point(0, 4)))
print(point_in_circle(cir, Point(130, 90)))  # True
print(point_in_circle(cir, Point(80, 30)))  # False

rect = Rectangle(40, 20, Point(120, 80))
print(rect_in_circle(cir, rect))  # True

# print(cir.center, cir.radius)
