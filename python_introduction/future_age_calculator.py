"""receive user input and calculate the user’s age in a future year."""

age = int(input("How old are you? "))
future_year = 2050
current_year = 2023

print(f'In {future_year}, you will be {age + (future_year - current_year)} years old.')
