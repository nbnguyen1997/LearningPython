import string

punctuation = string.punctuation


def make_dict():
    di = dict()
    fin = open(r".\Chapter13\book_text.txt")
    book_text = fin.read()
    di["total_word"] = 0

    list_word = book_text.split()

    for item in list_word:
        item = item.lower()
        if item[0] in punctuation or item[-1] in punctuation:
            word = handle_word(item)
            if word not in di:
                di[word] = 1
            else:
                di[word] += 1
        else:
            if item not in di:
                di[item] = 1
            else:
                di[item] += 1

        di["total_word"] += 1
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
list_word = []
for item in di:
    list_word.append((di[item], item))
list_word.sort(reverse=True)

for number, word in list_word[1:21]:
    print(number, word)
