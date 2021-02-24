def store_anagram(filename=r".\Chapter9\words.txt"):
    fin = open(filename, encoding="utf-8")

    result = dict()

    for line in fin:
        line = line.strip().lower()
        list_letter = list(line)
        list_letter.sort()
        string_sort = "".join(list_letter)

        if string_sort not in result:
            result[string_sort] = [line]
        else:
            result[string_sort].append(line)

    return result


def read_anagram(word, di):
    list_letter = list(word)
    list_letter.sort()

    string_sort = "".join(list_letter)

    if string_sort in di:
        return di[string_sort]
    else:
        return ""


# store = store_anagram()

# print(read_anagram("stop", store))
# line = "stop"
# list_letter = list(line)
# list_letter.sort()
# string_sort = "".join(list_letter)
# print(string_sort)