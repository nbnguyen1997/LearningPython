import string


def make_set(file_name):
    fin = open(file_name, encoding="UTF-8").read().lower()
    # fin = fin.replace("--", " ")
    # for i in fin:
    #     if ord(i) == 34:
    #         print(i)
    for i in string.punctuation:
        fin = fin.replace(i, " ")
    fin = fin.replace(chr(8220), " ")
    # ord("“") = 8220
    fin = fin.replace(chr(8221), " ")
    # ord("”") = 8221
    list_word = fin.split()
    # print(list_word)
    set_word = set(list_word)
    return set_word


link_emma = r".\Chapter12\emma.txt"
link_word = r".\Chapter9\words.txt"
# print(make_set(link_emma))
set_emma = make_set(link_emma)
set_word = make_set(link_word)

set_result = set_emma - set_word

print(set_result)
