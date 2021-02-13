import string

punctuation = string.punctuation


def read_file_to_list(file_name):
    result = []

    fin = open(file_name, encoding="utf-8")

    for line in fin:
        list_word_in_line = line.strip().split()
        for word in list_word_in_line:
            item = handle_word(word.lower())
            if item != "":
                result.append(item)

    return result


def handle_word(agr):
    word = agr

    if len(word) == 1:
        return ""

    while word[0] in punctuation:
        word = word[1:]
    while word[-1] in punctuation:
        word = word[:-1]

    return word


def make_dict_from_list(list_word):
    di = dict()
    for word in list_word:
        if word not in di:
            di[word] = 1
        else:
            di[word] += 1
    return di


def make_list_from_dict(di):
    result = []
    for word in di:
        result.append((di[word], word))
    return result


file_list_word = r".\Chapter9\words.txt"
file_book = r".\Chapter13.\book_text.txt"

list_word = read_file_to_list(file_list_word)
book = read_file_to_list(file_book)
dict_word_book = make_dict_from_list(book)
list_tuple_word_book = make_list_from_dict(dict_word_book)

number_word_not_in_list_words = 0
for word in book:
    if word not in list_word:
        # print(word)
        number_word_not_in_list_words += 1


print(
    "The number word in the book that are not in the word list %s"
    % (number_word_not_in_list_words)
)

list_tuple_word_book.sort(reverse=True)

number_common_word = 0
for number, word in list_tuple_word_book[0:1]:
    if word not in list_word:
        number_common_word += 1

print(
    "The number common words that should be in the word list: %s" % (number_common_word)
)
