from datetime import datetime, time
from datetime import *

today = date.today()
print("Current Year: ", today.year)
print("Current Month: ", today.month)
print("Current Day: ", today.day)

today_time = time()


# time: hour, minute second
current_time = time(9, 18, 22)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)


# print("Current Hour: ", today_time.hour)
# print("Current Minute: ", today_time.minute)
# print("Current Second: ", today_time.second)

full_date_time = datetime(2020, 7, 7, 11, 9, 11)
print(full_date_time)