class Point:
    x = 0
    y = 0


class Rectangle:
    width = 0
    height = 0
    cornor = Point()


def move_rectangle(rec, dx, dy):
    cornor = rec.cornor
    cornor.x += dx
    cornor.y += dy


def print_rec(rec):
    print(rec.cornor.x, " ", rec.cornor.y)


rec = Rectangle()
rec.width = 100
rec.height = 200
rec.cornor.x = 0
rec.cornor.y = 0

move_rectangle(rec, 50, 50)

print_rec(rec)