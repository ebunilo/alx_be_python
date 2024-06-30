"""Triangle pattern"""
rows = int(input("Enter the number of rows: "))
i = 0
j = 0
k = rows

while i < rows:
    print(" " * (k - 1), end="")
    print("*" * (j + 1), end="")
    print(end="\n")
    i += 1
    j += 2
    k -= 1

"""
Output:
     *
    ***
   *****
  *******
 *********
***********
"""