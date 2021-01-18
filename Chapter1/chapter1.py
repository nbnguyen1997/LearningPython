# Exercise 1-2
# 2.1 How many seconds are there in 42 minutes 42 seconds?
print(42*60+42)

# 2.2 How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
print(10/1.61)

# 2.3 If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average
# pace (time per mile in minutes and seconds)? What is your average speed in
# miles per hour?
print("time per miles in minutes")
print(10/(42+42/60))

print("time per miles in seconds")
print(10/(42*60+42))

print("average speed in miles per hour")
print(((42/60)+(42/3600))/10)