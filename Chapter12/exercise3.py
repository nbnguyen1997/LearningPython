def is_metathesis_pair(string_1, string_2):

    len_string = 0
    if len(string_1) != len(string_2):
        return False
    else:
        len_string = len(string_1)

    char_1 = None
    char_2 = None
    flag = 0
    flag_result = False
    for index in range(len_string):
        if string_1[index] != string_2[index]:
            flag += 1
            if flag == 2:
                if string_1[index] == char_2 and string_2[index] == char_1:
                    flag_result = True
                else:
                    flag_result = False
            char_1 = string_1[index]
            char_2 = string_2[index]
            if flag > 2:
                return False
    return flag_result


def make_dict():
    di = dict()
    fin = open(".\Chapter9\words.txt")
    """
    để giảm số lượng vòng lặp duyệt "word", ta sẽ tạo ra một "dictionary" với
    "key" là "length" của "word"
    "value" là list các "word" cùng "length"
    Việc cần làm tiếp theo chỉ là duyệt các "word" có cùng "length"
    và kiểm tra từng cặp xem chúng có phải là "metathesis pair" không?
    """
    for i in range(5000):
        string = fin.readline().strip().lower()
        length = len(string)
        # print(length,string)
        if length not in di:
            di[length] = [string]
        else:
            di[length].append(string)
        # di.get(length,[string]).append(string)
        # print(di)
        # di[length] = di.get(length,[string]).append(string)

    return di


def handle_list(list_string):
    for i in range(len(list_string) - 1):
        for j in range(i + 1, len(list_string)):
            if is_metathesis_pair(list_string[i], list_string[j]):
                print(list_string[i], list_string[j])


di = make_dict()
for key in di:
    handle_list(di[key])
# print(is_metathesis_pair("converse","conserve"))