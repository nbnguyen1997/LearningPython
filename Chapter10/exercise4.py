def chop(t):
    """
    Takes a list, modifies it by removing the first and last elements, and returns None.
    """
    del t[0]
    del t[-1]
    return None


if __name__ == "__main__":
    t = [1, 2, 3, 4, 5]
    chop(t)
    print(t)
