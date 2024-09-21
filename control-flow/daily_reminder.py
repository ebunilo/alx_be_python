""" 
Reminds the user about a single, priority task for 
the day based on time sensitivity.
"""

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

if time_bound == "yes":
    reminder = f"Reminder: '{task}' is a {
        priority} priority task that requires immediate attention today!"
else:
    reminder = f"Note: '{task}' is a {
        priority} priority task. Consider completing it when you have free time."

match priority:
    case "high":
        print(reminder)
    case "medium":
        print(reminder)
    case "low":
        print(reminder)
    case _:
        print("Reminder: Unknown")
