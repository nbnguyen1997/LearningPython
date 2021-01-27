fin = open(".\Chapter9\words.txt")

def version_1():
    t=[]
    for item in fin:
        t.append(item)
    return t

def version_2():
    t = []
    for item in fin:
        t = t + [item]
    return t

version_1()
version_2()
# version_2 ton nhieu thoi gian hon vi
# moi lan them 1 phan tu no phai tao 1 list moi va copy toan bo sang list moi