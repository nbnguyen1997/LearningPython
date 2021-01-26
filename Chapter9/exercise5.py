def handling_string(string):
    temp = string.lower()
    result=''
    for letter in temp:
        if letter == ' ' or is_exit_letter(letter,result):
            pass
        else:
            result+= letter
    
    return result

def is_exit_letter(letter,string):
    for item in string:
        if item == letter or item == letter.lower():
            return True
    
    return False

def uses_all(word,string_required):
    for letter in string_required:
        if is_exit_letter(letter,word):
            pass
        else:
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
    string_required = handling_string(input("Enter string of required letters: "))

    while True:
        word = check_input_word(input("Enter word ('done' to quick):"))
        if word == 'done' or word == 'Done':
            break
        print(uses_all(word,string_required))
    
check_input()
