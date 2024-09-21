""" 
Prompts the user to enter a positive integer, 
then use nested loops to print a square pattern 
of that size made of asterisks (*)
"""
size = int(input("Enter the size of the pattern: "))
ROW = 0

while ROW < size:
    for _ in range(size):
        print("*", end="")
    print()
    ROW += 1
