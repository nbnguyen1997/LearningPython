
def main():
    a = int(input("Nhap so a\n"))
    b = int(input("Nhap so b\n"))

    print(is_power(abs(a), abs(b)))


def is_power(a, b):
    """
        returns True if a is a power of b
    """
    if a == 0 and b == 0:
        return True
    if b == 0 and a != 0:
        return False
    if a % b == 0:
        if(a/b == 1):
            return True
        else:
            return is_power(a/b, b)
    if b**0 == a:
        return True

    return False


if __name__ == "__main__":
    main()
