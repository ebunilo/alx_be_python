"""Pattern drawing"""
size = int(input("Enter the size of the pattern: "))

n = size
while n > 0:
    for i in range(size):
        print("*", end="")
    print(end="\n")
    n -= 1