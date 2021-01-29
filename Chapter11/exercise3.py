cache = dict()

def ackermann(m, n):
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    key_string = str(m)+"-"+str(n)
    if (key_string) in cache:
        return cache[key_string]
    else:
        cache[key_string] = ackermann(m-1, ackermann(m, n-1))
        return cache[key_string]


print(ackermann(3, 4))
print(ackermann(3, 6))