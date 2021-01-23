def gcd(a,b):
    a = abs(a)
    b = abs(b)
    if a == 0 or b == 0:
        return a + b
    if a != b :
        if a > b :
            return gcd(a-b,b)
        else:
            return gcd(b-a,a)
    return a

def check_num():
    a = int(input("Enter number a\n"))
    b = int(input("Enter number b\n"))
    print(gcd(a,b))

check_num()