'''---------- Student Grade Calculator ------------------------------
Write a Python program that defines a function calculate_grade(marks).
The function should:
• Accept marks (0–100) as a parameter.
• Return the grade according to the following criteria:
o 90 and above → A+
o 75–89 → A
o 60–74 → B
o 40–59 → C
o Below 40 → Fail
The main program should:
• Accept marks of 5 students.
• Call the function for each student.
• Display the marks and corresponding grade.

---------------------------------------------------------------------'''

#--------------------------------------------------------------------

# Function to calculate grade
def calculate_grade(marks):

    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"

for i in range(1,6):

    print("Student", i)

    marks = int(input("Enter Marks : "))

    grade = calculate_grade(marks)

    print("Marks :", marks)
    print("Grade :", grade)
    print()
    
#---------------------------------------------------------------

''' Output :

Enter Marks of Student 1 : 95
Student 1 : Marks = 95 Grade = A+

Enter Marks of Student 2 : 82
Student 2 : Marks = 82 Grade = A

Enter Marks of Student 3 : 67
Student 3 : Marks = 67 Grade = B

Enter Marks of Student 4 : 55
Student 4 : Marks = 55 Grade = C

Enter Marks of Student 5 : 34
Student 5 : Marks = 34 Grade = Fail

'''