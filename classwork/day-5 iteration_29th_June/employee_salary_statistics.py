'''---------- Employee Salary Statistics ------------------
A company has N employees.

Accept the salary of each employee and determine:

• Highest Salary
• Lowest Salary
• Average Salary
• Number of Employees earning more than ₹50000

----------------------------------------------------------
Sample Input

Enter Number of Employees : 4

Employee 1 Salary : 45000
Employee 2 Salary : 60000
Employee 3 Salary : 80000
Employee 4 Salary : 35000

----------------------------------------------------------
Sample Output

Highest Salary : ₹80000
Lowest Salary : ₹35000
Average Salary : ₹55000.0
Employees earning above ₹50000 : 2
----------------------------------------------------------'''
#----------------------------------------------------------
#---------------- Coding ----------------------------------

# input number of employees
n = int(input("Enter Number of Employees : "))

# validate input
if(n <= 0):
    exit("Number of employees must be positive")

total = 0
count = 0

for i in range(1, n + 1):

    salary = float(input("Employee " + str(i) + " Salary : "))

    total += salary

    if(i == 1):
        highest = salary
        lowest = salary
    else:
        if(salary > highest):
            highest = salary

        if(salary < lowest):
            lowest = salary

    if(salary > 50000):
        count += 1

average = total / n

print("Highest Salary : ₹", highest)
print("Lowest Salary : ₹", lowest)
print("Average Salary : ₹", average)
print("Employees earning above ₹50000 :", count)

#----------------------------------------------------------

''' Output :
Enter Number of Employees : 4

Employee 1 Salary : 45000
Employee 2 Salary : 60000
Employee 3 Salary : 80000
Employee 4 Salary : 35000

Highest Salary : ₹80000
Lowest Salary : ₹35000
Average Salary : ₹55000.0
Employees earning above ₹50000 : 2
'''