from anagram_sets import store_anagram, read_anagram
import os

store = dict()
store = store_anagram()
word = "stop"
print(word, read_anagram(word, store))
print(os.listdir())
