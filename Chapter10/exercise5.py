def is_sorted(t):
    for index in range(len(t)-1):
        if t[index] > t[index +1]:
            return False
    return True

print(is_sorted([1,2,2,3]))
print(is_sorted(['a','b','a']))