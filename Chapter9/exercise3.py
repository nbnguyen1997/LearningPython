def handling_string(string):
    temp = "".join(string.split()).lower()
    result = ''.join({letter for letter in temp})

    return result


def avoids(word, forbidden_letter):
    """
    Returns True if the word doesn’t use any of the forbidden letters.
    """
    for letter in word:
        if letter in forbidden_letter:
            return False
    return True


def check_input():
    string_forbidden_letter = handling_string(
        input("Enter string of forbidden letters: "))

    while True:
        word = "".join(
            (input("Enter word ('done' to quick):")).split()).lower()
        if word == 'done' or word == 'Done':
            break
        print(avoids(word, string_forbidden_letter))


if __name__ == "__main__":
    check_input()
