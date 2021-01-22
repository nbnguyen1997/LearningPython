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

const = "nn01nn"
# print(first(const))
# print(last(const))
# print(len(middle(const)))
# print(const)
print(is_palindrome(const))