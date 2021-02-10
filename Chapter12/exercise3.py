def metathesis_pair(string_1,string_2):
    list_1 = list(string_1)
    list_2 = list(string_2)
    len_string = 0
    if len(list_1) != len(list_2):
        return False
    else:
        len_string = len(list_1)
    
    char_1 = None
    char_2 = None
    flag = 0
    for index in range(len_string):
        if list_1[index] != list_2[index]:
            flag += 1
            if flag == 2:
                if list_1[index] == char_2 and list_2[index] == char_1:
                    return True
                else:
                    return False
            char_1 = list_1[index]
            char_2 = list_2[index]
    





print(metathesis_pair("converse","conserve"))