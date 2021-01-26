fin = open(".\Chapter9\words.txt")

def has_no_e(string):
    for letter in string:
        if letter == 'e' or letter == 'E':
            return False
    return True

def print_no_e():
    count_word_no_e = 0
    total = 0
    for line in fin:
        word = line.strip()
        if has_no_e(word):
            count_word_no_e+=1
            print(word)
        total+=1
    print("The percentage of the words in the list that have no 'e':",count_word_no_e / total * 100 , "%")
    
print_no_e()
