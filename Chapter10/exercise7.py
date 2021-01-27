def has_duplicates(t):
    for i in range(len(t)-1):
        for j in range(i+1,len(t)):
            if t[i] == t[j]:
                return True
    return False

print(has_duplicates([1,2,3,4,5,4]))
