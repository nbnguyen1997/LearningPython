def reverse_string(string):
    result = ''
    for item in string:
        result = item +result
    return result

def check_reverse(first_word,second_word):
    if len(first_word) != len(second_word):
        return False
    else:
        return first_word == reverse_string(second_word)

print(check_reverse("abac","cbaa"))
print(check_reverse("abc","cba"))

