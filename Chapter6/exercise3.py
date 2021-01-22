def is_palindrome(string):
    if len(string) == 1:
        return True
    else:
        if first(string)==last(string):
            if(len(middle(string))==0):
                return True
            else:
                return is_palindrome(middle(string))
        else:
            return False

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

const = ""

def check_string():
    const = input("Enter string\n")
    if(len(const)):
        print(is_palindrome(const))
    else:
        print("The empty string")

check_string()
# print(first(const))
# print(last(const))
# print(len(middle(const)))
# print(const)
