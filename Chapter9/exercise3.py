def handling_string(string):
    temp = string.lower()
    result=''
    for letter in temp:
        if is_exit_letter(letter,result):
            pass
        else:
            result+= letter
    
    return result

def is_exit_letter(letter,string):
    for item in string:
        if item == letter or item == letter.lower():
            return True
    
    return False

def avoids(word,forbidden_letter):
    for letter in word:
        if is_exit_letter(letter,forbidden_letter):
            return False
    return True

def check_input_word(string):
    temp = string.strip()
    resutl=''
    for item in temp:
        if item == ' ':
            break
        resutl+=item
    return resutl


def check_input():
    string_forbidden_letter = handling_string(input("Enter string of forbidden letters: "))

    while True:
        word = check_input_word(input("Enter word ('done' to quick):"))
        if word == 'done' or word == 'Done':
            break
        print(avoids(word,string_forbidden_letter))
    
check_input()
