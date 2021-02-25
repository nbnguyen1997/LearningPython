class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second


def is_after(time1, time2):
    time_1 = time1.hour * 60 * 60 + time1.minute * 60 + time1.second
    time_2 = time2.hour * 60 * 60 + time2.minute * 60 + time2.second

    return time_1 > time_2


time1 = Time(2, 0, 0)
time2 = Time(3, 0, 0)

print(is_after(time1, time2))
