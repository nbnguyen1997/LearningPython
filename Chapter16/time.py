class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        print("%.2d: %.2d: %.2d" % (self.hour, self.minute, self.second))


def is_after(time1, time2):
    time_1 = time1.hour * 60 * 60 + time1.minute * 60 + time1.second
    time_2 = time2.hour * 60 * 60 + time2.minute * 60 + time2.second

    return time_1 > time_2


def increment(time1, time2):
    time = Time()

    time.hour = time1.hour + time2.hour
    time.minute = time1.minute + time2.minute
    time.second = time1.second + time2.second

    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1

    if time.hour >= 24:
        time.hour -= 24

    return time


time1 = Time(2, 0, 0)
time2 = Time(3, 0, 0)

print(is_after(time1, time2))

time = increment(time1, time2)

time.print_time()