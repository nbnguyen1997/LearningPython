def nested_sum(t):
    total = 0

    for item in t:

        if isinstance(item, list):

            for item_nest in item:

                total += item_nest
        else:

            total += item

    return total


if __name__ == "__main__":
    t = [[1, 2], [3], [4, 5, 6]]

    print("sum: ", t, end=" = ")

    print(nested_sum(t))
