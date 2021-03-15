def is_anagram(first_word, second_word):
    """
    Takes two strings and returns True if they are anagrams
    """
    if len(first_word) != len(second_word):
        return False

    length = len(first_word)
    first_list = list(first_word)
    second_list = list(second_word)

    first_list.sort()
    second_list.sort()

    return all(first_list[index] == second_list[index] for index in range(length - 1))


if __name__ == "__main__":
    print(is_anagram('nguyen', 'uyenng'))
    print(is_anagram("aaabbcccc", "bbccccaaa"))
