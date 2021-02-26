import time1


def time_to_int(time):
    if not valid_time(time):
        raise ValueError("invalid Time object in time_to_int")
    return time.hour * 3600 + time.minute * 60 + time.second


def int_to_time(seconds):
    time = time1.Time()

    time.minute, time.second = divmod(seconds, 60)

    time.hour, time.minute = divmod(time.minute, 60)

    return time


def valid_time(time):
    if time.minute >= 60 or time.second >= 60:
        return False
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False

    return True


def mul_time(time, number):
    seconds = time_to_int(time)
    seconds *= number

    return int_to_time(seconds)


def div_time(time, number):
    seconds = time_to_int(time)
    seconds /= number
    return int_to_time(seconds)


ti = time1.Time(1, 20, 30)

int_to_time(time_to_int(ti)).print_time()

mul_time(ti, 2).print_time()  # 02:41:00

print("the average pace (time per mile): %s /mile" % (div_time(ti, 5).string_time()))
