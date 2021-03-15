fin = open(".\Chapter9\words.txt")


def make_list():
    t = []
    for item in fin:
        t.append(item.strip())
    return t


def is_anagram(first_word, second_word):
    if len(first_word) != len(second_word):
        return False

    first_list = list(first_word)
    second_list = list(second_word)

    first_list.sort()
    second_list.sort()

    return all(first_list[index] == second_list[index] for index in range(len(first_list)))


def interlock(first_word, second_word):
    words = first_word + second_word

    word_list = make_list()

    for word in word_list:

        if is_anagram(word, words):

            print(word)


if __name__ == "__main__":
    interlock("shoe", "cold")
