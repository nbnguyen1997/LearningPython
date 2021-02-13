import string

punctuation = string.punctuation


def make_dict():
    di = dict()
    di["total_words"] = 0
    fin = open(".\Chapter13\mobyword2.txt", encoding="utf-8")
    book_string = fin.read()

    list_word = book_string.split()
    for i in list_word:
        if i[0] in punctuation or i[-1] in punctuation:
            item = handle_word(i)
            if item not in di:
                di[item] = 1
            else:
                di[item] += 1
        else:
            if i not in di:
                di[i] = 1
            else:
                di[i] += 1

        di["total_words"] += 1

    return di


def handle_word(word):

    agr = word
    if len(agr) == 1:
        return ""
    while agr[0] in punctuation:
        agr = agr[1:]

    while agr[-1] in punctuation:
        agr = agr[:-1]

    return agr


di = make_dict()

print("The total number of words in the book: %s" % (di["total_words"]))
print("The number of times each word is used:")

for item in di:
    if item != "total_words" and item != "":
        print(di[item], item)
