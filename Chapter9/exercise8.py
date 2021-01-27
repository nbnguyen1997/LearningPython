def check_num():
    for i in range(600001):
        if i == reverse_number(i):
            convert_number_to_string(i)

def reverse_number(number):
    resutl = 0
    number_copy = number
    while number_copy / 10 != 0 :
        resutl = resutl * 10 + number_copy % 10
        # print(resutl)
        number_copy = number_copy // 10
        # print(number_copy)
    return resutl

def convert_number_to_string(number):
    string_number = str(number)
    print('0-'*(6-len(string_number))+handling_number(string_number))

def handling_number(string_number):
    resutl = ''
    length = len(string_number)
    for index in range(length - 1):
        resutl += string_number[index] + '-'
    resutl += string_number[-1]    
    return resutl
# convert_number_to_string(123)
# print(handling_number('12398980123'))
# print('123-'+'23')
check_num()
