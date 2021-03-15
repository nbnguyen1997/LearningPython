import bisect
fin = open(".\Chapter9\words.txt")


def make_list():
    t = []
    for item in fin:
        t.append(item.strip())
    return t


def in_bisect_cheat(word_list, word):
    """Checks whether a word is in a list using bisection search.
    Precondition: the words in the list are sorted
    word_list: list of strings
    word: string
    """
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False

    return word_list[i] == word


def in_bisect(word_list, word):
    if len(word_list) == 0:
        return False
    index = len(word_list) // 2
    if word == word_list[index]:
        return True

    if word_list[index] > word:
        return in_bisect(word_list=word_list[:index], word=word)
    else:
        return in_bisect(word_list=word_list[index+1:], word=word)


def main():

    word_list = make_list()
    print(in_bisect(word_list=word_list, word="alien"))
    print(in_bisect_cheat(word_list=word_list, word="alien"))


if __name__ == "__main__":
    main()
