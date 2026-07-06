'''---------- Multiplication Table Generator ------------------
Write a Python program that accepts a number from
the user and displays its multiplication table
up to 20.

--------------------------------------------------------------
Sample Input
Enter Number : 8
--------------------------------------------------------------
Sample Output
8 x 1 = 8
8 x 2 = 16
...
8 x 20 = 160
--------------------------------------------------------------'''
#--------------------------------------------------------------
#---------------- Coding --------------------------------------

num = int(input("Enter Number : "))

for i in range(1, 21):
    print(num, "x", i, "=", num * i)

#--------------------------------------------------------------

''' Output :
Enter Number : 8
8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
...
8 x 20 = 160
'''