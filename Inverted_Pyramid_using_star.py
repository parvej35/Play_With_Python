"""
Python program to print inverted pyramid using star(*)

* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""

rows = int(input("Number of rows: "))

for i in range(rows, 0, -1):
    for j in range(0, rows - i):
        print(end=' ')
    for k in range(0, i):
        print('*', end=' ')

    print()
