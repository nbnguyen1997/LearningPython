def cumsum(t):
    resutl = []
    total = 0
    for item in t:
        total += item
        resutl.append(total)

    return resutl

print(cumsum([1,2,3]))