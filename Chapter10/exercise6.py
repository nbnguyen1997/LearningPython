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

print(is_anagram('nguyen','guyenn'))