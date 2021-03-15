fin = open(".\Chapter9\words.txt")


def car_talk():
    for line in fin:
        word = line.strip()
        if check_word(count_letter(word)):
            print(word)


def count_letter(word):
    """Returns the number of occurrences of the string of characters corresponding to each position

    Args:
        word ([string])

    Returns:
        [string]: example:  aabbcdee => 22112 ( 2a 2b 1c 1d 2e)
    """
    count_letter = 1
    resutl = ''
    length = len(word)
    for index in range(length - 1):
        if (word[index] == word[index + 1]):
            count_letter += 1
        else:
            resutl += str(count_letter)
            count_letter = 1
    resutl += str(count_letter)
    return resutl


def check_word(handled_string):
    """
    Return True if the word that has three consecutive pairs of letter
    """
    count_consecutive = 0
    for item in handled_string:
        if int(item) > 1:
            count_consecutive += 1
            if count_consecutive > 2:
                return True
        else:
            count_consecutive = 0
    return False


if __name__ == "__main__":
    car_talk()
