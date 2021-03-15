def cumsum(t):
    """
    Takes a list of numbers and returns the cumulative sum
    """
    resutl = []

    total = 0

    for item in t:

        total += item

        resutl.append(total)

    return resutl


if __name__ == "__main__":

    print(cumsum([1, 2, 3]))
