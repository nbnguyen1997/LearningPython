def rotate_word(string,number):
    """[returns the string after rotating]

    Args:
        string ([string]): [string to rotating]
        number ([number]): [number step to rotate]

    Returns:
        [string]

    """
    numer_index = 0
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

def function_input():
    string = input("Nhap chuoi: ")
    number = int(input("Nhap khoang cach xoay: "))

    print(rotate_word(string=string,number=number))

if __name__=="__main__":
    function_input()