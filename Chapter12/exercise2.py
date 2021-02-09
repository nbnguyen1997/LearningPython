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
# print("".join(['a', 'b', 'b', 'e', 'y']))
# print("".join(['a', 'a']))

print_di(di)