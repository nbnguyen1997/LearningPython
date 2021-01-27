def chop(t):
    del t[0]
    del t[-1]
    return None
t=[1,2,3,4,5]
chop(t)
print(t)
