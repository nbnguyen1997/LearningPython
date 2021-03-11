def is_triangle(a, b, c):
    if (a > b + c) or (b > a + c) or (c > a + b):
        return False
    return True


def check_numbers():
    a = int(input("Choose a number for a: "))
    b = int(input("Choose a number for b: "))
    c = int(input("Choose a number for c: "))
    return is_triangle(a=a, b=b, c=c)


if __name__ == "__main__":
    print(check_numbers())
