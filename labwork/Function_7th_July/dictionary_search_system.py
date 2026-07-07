'''-------------------Dictionary Search System------------------------------ 
Write a Python program that defines a function search_student(student_dict, roll_no).
The function should:
• Accept a dictionary where:
o Key = Roll Number
o Value = Student Name
• Search for the given roll number.
• Return the student name if found; otherwise return "Student Not Found".
The main program should:
• Create a dictionary of at least 5 students.
• Accept a roll number from the user.
• Display the search result.
-----------------------------------------------------------------------------'''

#-----------------------------------------------------------------------------

# Function to search student
def search_student(student_dict, roll_no):
    if roll_no in student_dict:
        return student_dict[roll_no]
    else:
        return "Student Not Found"

# Dictionary of students
students = {
    201: "Aman",
    202: "Priya",
    203: "Rahul",
    204: "Neha",
    205: "Sneha"
}

# Input from user
roll = int(input("Enter Roll Number: "))

# Function call
result = search_student(students, roll)

# Display result
print(result)

#--------------------------------------------------------------------

''' Output :
Enter Roll Number: 202
Priya

'''