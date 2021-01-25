def is_palindrome(string):
    # string = string.lower()
    # reversed_string = string.slice[::-1]
    # if(string == reversed_string):
    return string == string[::-1]

def function_input():
    print(is_palindrome(input("Enter string\n")))

function_input()