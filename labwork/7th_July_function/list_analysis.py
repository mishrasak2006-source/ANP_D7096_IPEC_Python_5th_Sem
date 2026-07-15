'''----------------List Analysis Using Functions-----------------
Write a Python program that defines the following functions:
• find_max(numbers)
• find_min(numbers)
• find_average(numbers)
The program should:
• Accept a list of 10 integers from the user.
• Call all three functions.
• Display the maximum value, minimum value, and average of the list.
---------------------------------------------------------------'''

#---------------------------------------------------------------

# function to find maximum
def find_max(numbers):
    return max(numbers)

# function to find minimum
def find_min(numbers):
    return min(numbers)

# function to find average
def find_average(numbers):
    return sum(numbers) / 10

# creating empty list to store integers from user
numbers = []

# input from user
print("Enter 10 Numbers")

# adding numbers to the list 
for i in range(10):
    num = int(input("Enter Number : "))
    numbers.append(num)

# display result
print("---------------------------------------------------------")
print("Maximum Number :", find_max(numbers))
print("Minimum Number :", find_min(numbers))
print("Average :", find_average(numbers))

#---------------------------------------------------------------
''' Output :

Enter 10 Numbers
Enter Number : 12
Enter Number : 64
Enter Number : 76
Enter Number : 38
Enter Number : 90
Enter Number : 5
Enter Number : 45
Enter Number : 35
Enter Number : 27
Enter Number : 59
--------------------------------------------------------------
Maximum Number : 90
Minimum Number : 5
Average : 45.1

'''