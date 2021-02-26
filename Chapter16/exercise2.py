import datetime


def check_date(date):
    year = date.year
    month = date.month
    day = date.day

    list_month_1 = [1, 3, 5, 7, 8, 10, 12]
    list_month_2 = [4, 6, 9, 11]

    if day < 1 or month < 1 or month > 12:
        return False

    if month in list_month_1:
        if day > 31:
            return False
    elif month in list_month_2:
        if day > 30:
            return False
    elif month == 2:
        if check_year(year):
            if day > 29:
                return False
        else:
            if day > 28:
                return False
    return True


def check_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


def get_year(date1, date2):
    return


da = datetime.date.today()
# month = datetime.year(da)
# print(month)
bit = datetime.date(2000, 2, 14)
print(check_date(bit))
# print(dir(da.max.day))

# print("Today is %s " % (da.strftime("%A")))