def make_dict(t):
    d =  dict() 
    for item in t:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    return d

def has_duplicates(word):
    d = make_dict(word)
    val = d.values()
    if 2 in val:
        return True
    else:
        return False

print(has_duplicates("nguyen"))