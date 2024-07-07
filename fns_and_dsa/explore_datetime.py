from datetime import timedelta
from datetime import datetime

def display_current_datetime():
    """Displays the current date and time"""

    # Get the current date and time
    now = datetime.now()
    print('Current date and time: ', now.strftime("%Y-%m-%d %H:%M:%S" ))


def calculate_future_date():
    """Calculate future date"""
    delta = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=delta)

    print("Future date: ", future_date.strftime("%Y-%m-%d" ))
