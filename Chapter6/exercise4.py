
def check_num():
    a = int(input("Nhap so a\n"))
    b = int(input("Nhap so b\n"))

    print(is_power(abs(a),abs(b)))

def is_power(a,b):
    if a == 0 and b == 0:
        return True
    elif b==0 and a!=0:
        return False
    elif a % b == 0:
        if(a/b == 1):
            return True
        else:
            return is_power(a/b,b)
    elif b**0 == a:
        return True
    else:
        return False


check_num()
# print(int("-2"))