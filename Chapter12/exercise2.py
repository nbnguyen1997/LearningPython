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

def print_dict_max_len(di):
    max_len = 0
    key_max =""
    for key in di:
        len_result = len(di[key])
        # if len_result > 1 :
        #     print(di[key])
        
        if len_result > max_len:
            max_len = len_result
            key_max = key

    return di[key_max]
# print("".join(['a', 'b', 'b', 'e', 'y']))
# print("".join(['a', 'a']))

print(print_dict_max_len(di))