""" 
Asks the user to enter a number, then use a for loop to print 
the multiplication table for that number from 1 to 10.
"""
number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
