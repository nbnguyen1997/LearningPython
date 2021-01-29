def rotate_word(string,number):
    numer_index = 0
    number_step = 0
    result=""
    for item in string:
        number_char = ord(item)
        if 65 <= number_char <=90:
            number_index = 65
        elif 97 <= number_char <= 122:
            number_index=97
        else:
            print("Chuoi chi chua cac ky tu a-z,A-Z")
            return
        number_char = ( number_char - number_index + number) % 26 + number_index
        result += chr(number_char)
    return result


def make_word_dict():
    d = dict()
    fin = open(".\Chapter9\words.txt")
    for line in fin:
        word = line.strip().lower()
        d[word] = None

    return d


def rotate_pairs(word, word_dict):
    for i in range(1, 14):
        rotated = rotate_word(word, i)
        if rotated in word_dict:
            print(word, i, rotated)


word_dict = make_word_dict()

for word in word_dict:
    rotate_pairs(word, word_dict)