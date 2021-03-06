"""
@Author: Parvej Chowdhury
@Time: 01-Jun-22 1:10 AM

Python program to print pyramid using star (*)
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""

if __name__ == "__main__":
    rows = int(input("Number of rows: "))

    counter = 0

    for row in range(1, (rows + 1)):
        for space in range(1, (rows - row) + 1):
            print(end = "  ") # double space

        while counter != (2 * row - 1):
            print("* ", end="")
            counter += 1

        counter = 0 #reset counter
        print()

