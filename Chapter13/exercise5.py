import random
from fractions import *


def histogram(t):
    di = dict()
    for item in t:
        if item not in di:
            di[item] = 1
        else:
            di[item] += 1
    return di


def choose_from_hist(hist):
    total = 0
    for key in hist:
        total += hist[key]
        # print(hist[key], key)
    list_from_dict = list(hist.items())
    key, Value = random.choice(list_from_dict)
    # print(key)
    print("'%s' with probability %s" % (key, Fraction(hist[key], total)))


t = ["a", "b", "a", "c", "c", "c", "c"]
# print(histogram(t))
choose_from_hist(histogram(t))
# print(Fraction(3, 4))
