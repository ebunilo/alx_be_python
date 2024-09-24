""" 
Check for prime numbers in range 2 to 10
"""
for n in range(2, 10):
    for x in range(2, n):
        # print(f"n: {n}")
        # print(f"x: {x}")
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
