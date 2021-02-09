def handle_file():
    di = dict()
    fin = open(".\Chapter9\words.txt")
    di_reverse = dict()
    for item in fin:
        line = item.strip().lower()

        list_string = list(line)

        list_string.sort()

        result = "".join(list_string)
        
        
        if result not in di_reverse:
            di_reverse[result] = [line]
        else:
            di_reverse[result].append(line)
        
        
    
    
    
    return di_reverse

di = handle_file()

def print_di(di):
    for key in di:
        if len(di[key]) > 1 :
            print(di[key])

def print_dict_order(di,len_bingo = 1):
    list_item = []

    if len_bingo == 1:
        for value in di.values():
            if len(value) > len_bingo :
                list_item.append((len(value),value))
    else:
        for value in di.values():
            if len(value) == len_bingo :
                list_item.append((len(value),value))

    list_item.sort()

    for item in list_item:
        print(item)


# print_dict_order(di)

print_dict_order(di,8)
