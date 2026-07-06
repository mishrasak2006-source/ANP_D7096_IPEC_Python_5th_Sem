'''---------- Scholarship Eligibility ------------------
A university provides a scholarship only to students
who score 90 or above.

Write a Python program to accept a student's
percentage and determine whether the student
is eligible.

--------------------------------------------------------
Sample Input
Enter Percentage : 92
--------------------------------------------------------
Sample Output
Scholarship Approved
--------------------------------------------------------'''
#--------------------------------------------------------

# input of percentage
percentage = float(input("Enter Percentage : "))

# validate percentage
if(percentage < 0 or percentage > 100):
    exit("Percentage must be between 0 and 100")

# checking scholarship eligibility
if(percentage >= 90):
    print("Scholarship Approved")
else:
    print("Scholarship Not Approved")

#--------------------------------------------------------

''' Output :
Enter Percentage : 92
Scholarship Approved
'''