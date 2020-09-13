from datetime import date, datetime, time
from datetime import *

now = datetime.now()

print(now)


time = now.strftime("%H:%M:%S")

longer_time = now.strftime("%m/%d/%Y, %H:%M:%S")

print(time)

print(longer_time)