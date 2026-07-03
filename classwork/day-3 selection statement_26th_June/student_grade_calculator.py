'''---------- Student Grade Calculator ------------------
A school assigns grades based on the marks obtained
by students according to the following criteria:

• Marks 90 and above  -> Grade A
• Marks 75 to 89      -> Grade B
• Marks 50 to 74      -> Grade C
• Below 50            -> Grade F

Write a Python program to accept marks from the user
and display the corresponding grade.
--------------------------------------------------------
Sample Input
Enter Marks: 92
--------------------------------------------------------
Sample Output
Grade A
--------------------------------------------------------
Sample Input
Enter Marks: 80
--------------------------------------------------------
Sample Output
Grade B
--------------------------------------------------------
Sample Input
Enter Marks: 65
--------------------------------------------------------
Sample Output
Grade C
--------------------------------------------------------
Sample Input
Enter Marks: 35
--------------------------------------------------------
Sample Output
Grade F
--------------------------------------------------------'''
#--------------------------------------------------------
#---------------- Coding --------------------------------

# input of marks from user
marks = float(input("Enter Marks : "))

# validate marks
if(marks < 0 or marks > 100):
    exit("Marks must be between 0 and 100")

# checking grade
if(marks >= 90):
    print("Grade A")
elif(marks >= 75):
    print("Grade B")
elif(marks >= 50):
    print("Grade C")
else:
    print("Grade F")

#--------------------------------------------------------

''' Output :
Enter Marks : 92
Grade A
'''