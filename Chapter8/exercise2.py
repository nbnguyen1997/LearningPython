def count_sub(sub,string):
    count = 0
    index = 0
    while index < len(string)-len(sub)+1:
        if string[index] == sub[0]:
            result = True
            j = 0
            while j < len(sub):
                if index + j >= len(string) or string[index+j] != sub[j]:
                    resutl = False
                else:
                    print(index+j,string[index+j],j,sub[j])
                    
                j+=1
            if ( result == True):
                count += 1
        index+=1    

    return count

print (count_sub('ana','banana'))
    
