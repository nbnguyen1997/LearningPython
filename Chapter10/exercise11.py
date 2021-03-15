def reverse_string(string):
    """
    Return the string reversed
    """
    return string[::-1]


def is_reverse(first_word, second_word):
    if len(first_word) != len(second_word):
        return False
    else:
        return first_word == reverse_string(second_word)


if __name__ == "__main__":
    print("abac, cbaa : ", is_reverse("abac", "cbaa"))
    print("abc, cba: ", is_reverse("abc", "cba"))
