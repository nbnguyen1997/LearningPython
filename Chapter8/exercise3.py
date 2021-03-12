def is_palindrome(string):
    """[returns True if it is a palindrome and False otherwise]

    Args:
        string ([string]): [string to check]

    Returns:
        [bool]
    """
    return string == string[::-1]

def function_input():
    print(is_palindrome(input("Enter string\n")))

if __name__ == "__main__":
    function_input()