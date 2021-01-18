
# Exersice 2-2
# 2.1 The volume of a sphere with radius r is 4 3πr3. What is the volume of a sphere with
# radius 5?

pi = 3.141592654
r = 5
print("The volume of a sphere with radius r = 5")
print(r**3*pi*4/3)

# 2.2 Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy. What is
# the total wholesale cost for 60 copies?
quantity = 60
print(quantity * 24.95 * 0.4 + 3 + (quantity - 1) * 0.75)

# 2.3 If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then
# 3 miles at tempo (7:12 per mile) and 1 mile at an easy pace again, what time do I
# get home for breakfast?

time_leave_home = 6*60*60 + 52*60
time_run = 2 * (8 * 60 + 15) + 3 * (7 * 60 + 12)
time_get_home = time_leave_home + time_run
minutes = time_get_home % 3600
second = minutes % 60
minutes = (minutes -second) / 60
hour = (time_get_home - minutes * 60 - second) / 3600
print(int(hour),':',int(minutes),':',int(second))
