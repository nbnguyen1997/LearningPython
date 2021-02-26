import datetime
import time


def birthday(birthday):
    cur = datetime.datetime.today()
    age = cur.year - birthday.year
    birthday_in_year = datetime.datetime(cur.year, birthday.month, birthday.day)

    days = (cur - birthday_in_year).days

    days_of_birth = 0
    if days < 0:
        days_of_birth = -days
    if days > 0:
        date = datetime.datetime(cur.year + 1, birthday.month, birthday.day)
        days_of_birth = (date - cur).days

    print("Your current age is %d" % age)

    if days_of_birth == 0:
        print("Happy birth day to you!!!")
    else:
        print(
            "Your next birthday: %d day, %.2d:%.2d:%.2d"
            % (days_of_birth - 1, 23 - cur.hour, 59 - cur.minute, 60 - cur.second)
        )


da = datetime.datetime.today()

birth_day = datetime.datetime(2000, 2, 26)

birth_day_2 = datetime.datetime(2000, 1, 1)


print("Today is %s " % (da.strftime("%A")))
birthday(birth_day)
print()
birthday(birth_day_2)