def reverse_number(number):
    resutl = 0

    number_copy = number

    while number_copy / 10 != 0:

        resutl = resutl * 10 + number_copy % 10

        number_copy = number_copy // 10

    return resutl


def find_age(number):
    count = 0

    flag = False

    for age_mom_at_born in range(18, 80):

        for your_mom_age_currently in range(age_mom_at_born, 100):

            your_age_currently = your_mom_age_currently - age_mom_at_born

            if reverse_number(your_mom_age_currently) == your_age_currently:

                count += 1

                if count == number:

                    print("your'age current : ", your_age_currently)

                    print("your mom's age current: ", your_mom_age_currently)

                    count = 0

                    flag = True

                    break
        count = 0


if __name__ == "__main__":
    find_age(8)
