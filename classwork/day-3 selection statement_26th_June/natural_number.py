'''---------- Natural Number Check ------------------
A natural number is a positive integer (1, 2, 3, ...).
Write a Python program that accepts a number and
determines whether it is a natural number or not.
----------------------------------------------------
Sample Input
Enter a Number: 15
----------------------------------------------------
Sample Output
15 is a Natural Number.
----------------------------------------------------
Sample Input
Enter a Number: -8
----------------------------------------------------
Sample Output
-8 is Not a Natural Number.
----------------------------------------------------'''
#----------------------------------------------------
#---------------- Coding ----------------------------

# input of number from user
num = int(input("Enter a Number : "))

# checking whether the number is natural or not
if(num > 0):
    print(num, "is a Natural Number.")
else:
    print(num, "is Not a Natural Number.")

#----------------------------------------------------

''' Output :
Enter a Number : 15
15 is a Natural Number.
'''