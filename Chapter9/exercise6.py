def check_word(word):
    """
    Returns True if the letters in a word appear 
    in alphabetical order (double letters are okay)
    """
    for index in range(len(word)-1):
        if ord(word[index]) - ord(word[index + 1]) > 0:
            return False
    return True


def main():

    while True:
        word = "".join((input("Enter word (done to quick): ")).split()).lower()
        if word == 'done' or word == 'Done':
            break
        print(check_word(word))


if __name__ == "__main__":
    main()
