# kiem tra ky tu dau tien co phai lower hay khong
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False


# ham luon tra ve chuoi 'True'
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


# kiem tra ky tu cuoi cung co phai lower hay khong
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag


# kiem tra chuoi co ton tai ky tu lower hay khong
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

# ham tra ve False neu chuoi ton tai ky tu upper
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

