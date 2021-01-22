import time

time_days = 24*60*60
time_hours = 60*60
time_minutes = 60


times = time.time()

days = times//time_days
times = times%time_days
hours = times//time_hours
times = times %time_hours
minutes = times // time_minutes
times = times - minutes*time_minutes


print(times)
print(int(days),end=' day, time:: ')
print(int(hours),end=':')
print(int(minutes),end='\':')
print(times,end='\'\':')