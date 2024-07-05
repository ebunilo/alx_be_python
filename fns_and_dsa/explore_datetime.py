"""Displays the current date and time, and calculates
a future date"""

from datetime import timedelta
from datetime import datetime

# Get the current date and time
now = datetime.now()
print('Current date and time: ', now.strftime("%Y-%m-%d %H:%M:%S" ))

delta = int(input("Enter the number of days to add to the current date: "))
future_date = now + timedelta(days=delta)

print("Future date: ", future_date.strftime("%Y-%m-%d" ))
