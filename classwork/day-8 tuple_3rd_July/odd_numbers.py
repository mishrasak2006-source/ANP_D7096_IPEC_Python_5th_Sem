'''---------- Display Odd Numbers from a Tuple ------------------
Write a Python program to create a tuple of 15
numbers entered by the user and display all the
odd numbers present in that tuple.

----------------------------------------------------------
Sample Input
Enter Number 1 : 12
Enter Number 2 : 45
Enter Number 3 : 18
...
Enter Number 15 : 33

----------------------------------------------------------
Sample Output
Tuple : (12, 45, 18, ..., 33)

Odd Numbers :
45
33
----------------------------------------------------------'''
#----------------------------------------------------------
#---------------- Coding ----------------------------------

# create an empty list
lst = []

# input 15 numbers
for i in range(15):
    num = int(input("Enter Number " + str(i+1) + " : "))
    lst.append(num)

# convert list into tuple
tup = tuple(lst)

# display tuple
print("Tuple :", tup)

# display odd numbers
print("Odd Numbers :")

for i in tup:
    if(i % 2 != 0):
        print(i)

#----------------------------------------------------------

''' Output :
Enter Number 1 : 12
Enter Number 2 : 45
Enter Number 3 : 18
Enter Number 4 : 27
Enter Number 5 : 40
Enter Number 6 : 15
Enter Number 7 : 22
Enter Number 8 : 19
Enter Number 9 : 30
Enter Number 10 : 11
Enter Number 11 : 50
Enter Number 12 : 17
Enter Number 13 : 60
Enter Number 14 : 33
Enter Number 15 : 8

Tuple : (12, 45, 18, 27, 40, 15, 22, 19, 30, 11, 50, 17, 60, 33, 8)

Odd Numbers :
45
27
15
19
11
17
33
'''