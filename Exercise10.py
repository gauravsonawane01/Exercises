"""
Date Operations:
Print Today's Date
Print Current Time
Print Today's Day(like Mon-Sun)
Print Current Month
Print Date yesterday's and tomorrow's date

"""

from datetime import timedelta, datetime
from datetime import date
current = date.today()

# strftime() creates string representing date in various formats
print("\n")
print("Let's print date, month and year in different-different ways")
format1 = current.strftime("%m/%d/%y")

# prints in month/date/year format
print("Todays date =", format1)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

print("Todays day =", current.strftime('%A'))

print("Current Month is :", current.strftime('%B'))


# Tomorrows date
tomorrow = current + timedelta(days=1)
print('Tomorrows date:', tomorrow)

# Yesterdays date
yesterday = current - timedelta(days=1)
print('Yesterdays date :', yesterday)
