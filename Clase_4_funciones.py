#Patterns can be printed in python using simple for loops.
# First outer loop is used to handle number of rows and Inner nested loop is used to handle the number of columns.
# Manipulating the print statements, different number patterns, alphabet patterns or star patterns can be printed
# Hacer una fincion que imprima

def figura(n):
# Function to demonstrate printing pattern
# outer loop to handle number of rows
# n in this case
    for i in range(0, n):
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
            # printing stars
            print("* ",end="")
            # ending line after each row
        print("\r")

    # Driver Code
n = 5 ### Number of colunms
figura(n)