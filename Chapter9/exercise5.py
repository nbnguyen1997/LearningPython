def handling_string(string):
    """
    Return set lletter of the string
    """
    temp = ''.join(string.split())
    result = ''.join({item for item in temp})

    return result


def uses_all(word, string_required):
    """
    Returns True if the word uses all the required letters at least once
    """
    for letter in string_required:
        if letter in word:
            pass
        else:
            return False
    return True


def main():
    string_required = handling_string(
        input("Enter string of required letters: "))

    while True:
        word = input("Enter word ('done' to quick):")
        if word == 'done' or word == 'Done':
            break
        print(uses_all(word, string_required))


if __name__ == "__main__":
    main()
