def handling_string(string):
    temp = "".join(string.split()).lower()
    result = ''.join({item for item in temp})

    return result


def uses_only(word, string_letter):
    for letter in word:
        if letter in string_letter or letter == ' ':
            pass
        else:
            return False
    return True


def check_input():
    string_letter = handling_string(input("Enter string of letters: "))

    while True:
        word = input("Enter word ('done' to quick):")
        if word == 'done' or word == 'Done':
            break
        print(uses_only(word, string_letter))


if __name__ == "__main__":
    check_input()
