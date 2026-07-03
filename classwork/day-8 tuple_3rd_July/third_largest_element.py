'''---------- Third Largest Number in a List ------------------
Write a Python program to find the third largest
number from a list of 20 numbers entered by the user.'''

#---------------------------------------------------------
# create an empty list
lst = []

# input 20 numbers
for i in range(20):
    num = int(input("Enter Number : "))
    lst.append(num)

# sort the list in descending order
lst.sort(reverse=True)

# display third largest number
print("Third Largest Number :", lst[2])
#-------------------------------------------------------------

'''Sample Input
Enter Number : 12
Enter Number : 45
Enter Number : 90
Enter Number : 78
Enter Number : 56
Enter Number : 23
Enter Number : 11
Enter Number : 67
Enter Number : 89
Enter Number : 10
Enter Number : 34
Enter Number : 99
Enter Number : 54
Enter Number : 43
Enter Number : 76
Enter Number : 65
Enter Number : 87
Enter Number : 32
Enter Number : 21
Enter Number : 50
#--------------------------------------------------------------
 Output :
Enter Number : 12
Enter Number : 45
Enter Number : 90
Enter Number : 78
Enter Number : 56
Enter Number : 23
Enter Number : 11
Enter Number : 67
Enter Number : 89
Enter Number : 10
Enter Number : 34
Enter Number : 99
Enter Number : 54
Enter Number : 43
Enter Number : 76
Enter Number : 65
Enter Number : 87
Enter Number : 32
Enter Number : 21
Enter Number : 50

Third Largest Number : 89
'''