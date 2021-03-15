def is_sorted(t):
    """
    Takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise
    """
    return all(t[i] <= t[i+1] for i in range(len(t)-1))


if __name__ == "__main__":
    print(is_sorted([1, 2, 2, 3]))
    print(is_sorted(['a', 'b', 'a']))
