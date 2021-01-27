fin = open(".\Chapter9\words.txt")

def car_talk():
    for line in fin:
        word = line.strip()
        if check_word(count_letter(word)):
            print(word)

def count_letter(word):
    count_letter = 1
    resutl =''
    length = len(word)
    for index in range( length - 1 ):            
        if ( word[ index ] == word[ index + 1 ] ):
            count_letter += 1
        else:
            resutl += str(count_letter)
            count_letter = 1
    resutl += str(count_letter)
    return resutl

def check_word(handled_string):
    count_consecutive = 0
    for item in handled_string:
        if int(item) > 1 :
            count_consecutive += 1
            if count_consecutive > 2 :
                return True
        else:
            count_consecutive = 0
    return False

car_talk()

