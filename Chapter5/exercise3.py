def is_triangle(a, b, c):
    if (a > b + c ) or ( b > a + c ) or ( c > a + b ):
        print("No")
    else:
        print("Yes")

def check_numbers():
    a = int(input("Choose a number for a: "))
    b = int(input("Choose a number for b: "))
    c = int(input("Choose a number for c: "))
    return is_triangle(a = a , b = b, c = c)

check_numbers()