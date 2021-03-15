def has_duplicates(t):
    """
    Takes a list and returns True if there is any element that appears more than once
    """
    temp = t
    temp.sort()

    return any(temp[index] == temp[index+1] for index in range(len(temp)-1))


if __name__ == "__main__":
    print(has_duplicates([1, 2, 3, 4, 5, 4]))
    print(has_duplicates(['a', 'b', 'c', 'd', 'b']))
