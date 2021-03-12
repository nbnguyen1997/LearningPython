def gcd(a, b):
    """
    returns the greatest common divisor.
    """
    a = abs(a)
    b = abs(b)
    if a == 0 or b == 0:
        return a + b
    if a != b:
        if a > b:
            return gcd(a-b, b)
        else:
            return gcd(b-a, a)
    return a


def main():
    a = int(input("Enter number a\n"))
    b = int(input("Enter number b\n"))
    print(gcd(a, b))


if __name__ == "__main__":
    main()
