def check_word(word):
    for index in range(len(word)-1):
        if ord(word[index]) - ord(word[index + 1]) > 0:
            return False
    return True

def check_input_word(string):
    temp = string.strip()
    resutl = ''
    for letter in temp:
        if letter == ' ':
            return resutl
        resutl += letter
    return resutl

def function_input():
    
    while True:
        word = check_input_word(input("Enter word (done to quick): "))
        if word == 'done' or word == 'Done':
            break
        print(check_word(word))

function_input()