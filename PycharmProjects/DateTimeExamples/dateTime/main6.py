from datetime import date, datetime, time
from datetime import *

date_string = "July 24, 2020"
print(date_string)


date_object = datetime.strptime(date_string, "%B %d, %Y")

print(date_object)