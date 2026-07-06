'''---------- Student Result Analyzer ------------------
A teacher wants to analyze the marks of N students.

Accept the marks of each student (out of 100).

Finally display:
• Highest Marks
• Lowest Marks
• Average Marks
• Number of students who passed (Marks >= 40)
• Number of students who scored distinction (Marks >= 75)

--------------------------------------------------------
Sample Input
Enter Number of Students : 5

Student 1 Marks : 80
Student 2 Marks : 65
Student 3 Marks : 35
Student 4 Marks : 92
Student 5 Marks : 76

--------------------------------------------------------
Sample Output
Highest Marks : 92
Lowest Marks : 35
Average Marks : 69.6
Students Passed : 4
Students with Distinction : 3
--------------------------------------------------------'''
#--------------------------------------------------------
#---------------- Coding --------------------------------

# input number of students
n = int(input("Enter Number of Students : "))

# validate input
if(n <= 0):
    exit("Number of students must be positive")

total = 0
pass_count = 0
distinction = 0

for i in range(1, n + 1):

    marks = float(input("Student " + str(i) + " Marks : "))

    total += marks

    if(i == 1):
        highest = marks
        lowest = marks
    else:
        if(marks > highest):
            highest = marks
        if(marks < lowest):
            lowest = marks

    if(marks >= 40):
        pass_count += 1

    if(marks >= 75):
        distinction += 1

average = total / n

print("Highest Marks :", highest)
print("Lowest Marks :", lowest)
print("Average Marks :", average)
print("Students Passed :", pass_count)
print("Students with Distinction :", distinction)

#--------------------------------------------------------

''' Output :
Enter Number of Students : 5

Student 1 Marks : 80
Student 2 Marks : 65
Student 3 Marks : 35
Student 4 Marks : 92
Student 5 Marks : 76

Highest Marks : 92
Lowest Marks : 35
Average Marks : 69.6
Students Passed : 4
Students with Distinction : 3
'''