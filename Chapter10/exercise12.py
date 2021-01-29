fin = open(".\Chapter9\words.txt")
def make_list():
    t = []
    for item in fin:
        t.append(item.strip())
    return t


def is_anagram(first_word,second_word):
    if len(first_word) != len(second_word):
        return False
    
    first_list = list(first_word)
    second_list = list(second_word)

    first_list.sort()
    second_list.sort()

    for index in range(len(first_list)):
        if first_list[index] != second_list[index]:
            return False
    return True

def in_bisect(word_list,word):
    # if len(word_list) == 0 :
    #     return False
    # index = len(word_list) // 2
    # if word == word_list[index]:
    #     return T
    
    # if word_list[index] > word:
    #     return in_bisect(word_list=word_list[:index],word=word)
    # else:
        # return in_bisect(word_list=word_list[index+1:],word=word)
    
    for item in word_list:
        if is_anagram(item,word):
            print(item)

def interlock(first_word,second_word):
    words = first_word + second_word
    
    word_list = make_list()
    print(first_word,second_word)
    in_bisect(word_list=word_list,word=words)

interlock("shoe","cold")
