def main():
    for i in range(600001):

        if is_reverse(i):

            convert_number_to_string(i)


def is_reverse(number):
    if number == reverse_number(number):

        return True

    return False


def reverse_number(number):
    """
    Return the number reversed
    """
    resutl = 0

    number_copy = number

    while number_copy / 10 != 0:

        resutl = resutl * 10 + number_copy % 10

        number_copy = number_copy // 10

    return resutl


def convert_number_to_string(number):
    string_number = str(number)

    print('0-'*(6-len(string_number))+handling_number(string_number))


def handling_number(string_number):
    resutl = ''

    length = len(string_number)

    for index in range(length - 1):

        resutl += string_number[index] + '-'

    resutl += string_number[-1]

    return resutl


if __name__ == "__main__":
    main()
