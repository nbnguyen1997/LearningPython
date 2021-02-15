import string
import random
from bisect import bisect


def make_dict(link_file):
    fin = open(link_file, encoding="utf-8").read().lower()
    for char in fin:
        if char in string.punctuation:
            fin = fin.replace(char, " ")

    fin = fin.replace(chr(8220), " ")
    # ord("“") = 8220

    fin = fin.replace(chr(8221), " ")
    # ord("”") = 8221

    fin = fin.split()

    di = dict()

    for item in fin:
        di[item] = di.get(item, 0) + 1
    # print(di)
    return di


def make_list_frequencies(histogram):
    total_frequency = 0
    result = dict()

    for item in histogram:
        total_frequency += histogram[item]
        result[item] = result.get(item, total_frequency)

    # print(result)
    return result


def random_word(histogram):
    list_key = list(histogram.keys())
    list_value = list(histogram.values())
    # print(list_key)
    # print(list_value)

    # print(list_value[-1] - 1)
    x = random.randint(0, list_value[-1] - 1)
    index = bisect(list_value, x)

    print(index)

    return list_key[index]


link_emma = r".\Chapter12\emma.txt"
link_test = r".\Chapter13\filetest.txt"
print(random_word(histogram=make_list_frequencies(histogram=make_dict(link_test))))
#
# di = {"a": 2, "b": 2, "c": 3, "d": 1}
# list_key = di.keys()
# list_value = di.values()
# print(list_key)
# print(list_value)