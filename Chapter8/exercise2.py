def count_sub(sub,string):
    """[count the number of sub_string in the string]

    Args:
        sub ([string]): [sub string]
        string ([string]): [main string]

    Returns:
        [number]: [the number of occurrences of the substring in the string]
    """
    count = 0
    length_sub = len(sub)
    for index in range(len(string)):
        if sub[0] == string[index]:
            if sub == string[index:index+length_sub]:
                count+=1

    return count

if __name__ =="__main__":
    print (count_sub('anan','banana'))
    print(count_sub("aa","aaaaaa"))