'''---------- Loan Eligibility Check ----------------------
A bank considers an applicant eligible for a personal loan
only if their monthly salary is ₹30000 or more.
Write a Python program that accepts the monthly salary and
checks whether the applicant is eligible.
----------------------------------------------------------
Sample Input
Enter Monthly Salary: 45000
----------------------------------------------------------
Sample Output
Congratulations! You are eligible to apply for the loan.
----------------------------------------------------------
Sample Input
Enter Monthly Salary: 22000
----------------------------------------------------------
Sample Output
Sorry! You are not eligible to apply for the loan.
----------------------------------------------------------'''
#----------------------------------------------------------
#---------------- Coding ----------------------------------

# input of monthly salary
salary = float(input("Enter Monthly Salary : "))

# validate salary
if(salary <= 0):
    exit("Salary must be positive")

# checking loan eligibility
if(salary >= 30000):
    print("Congratulations! You are eligible to apply for the loan.")
else:
    print("Sorry! You are not eligible to apply for the loan.")

#----------------------------------------------------------

''' Output :
Enter Monthly Salary : 45000
Congratulations! You are eligible to apply for the loan.
'''