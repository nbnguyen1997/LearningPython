def nested_sum(t):
    total = 0
    for item in t:
        for item_nest in item:
            total += item_nest

    return total

t = [[1,2],[3],[4,5,6]]
print(nested_sum(t))