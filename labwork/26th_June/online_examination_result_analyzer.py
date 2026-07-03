'''---------- Online Examination Result Analyzer --------------
A student appears in 5 subjects.

Rules:
• Minimum 40 marks in every subject to pass.
• Distinction -> Average >=75
• First Division -> Average >=60
• Second Division -> Average >=50
• Pass -> Average >=40
• Fail if any subject <40

--------------------------------------------------------------'''
#--------------------------------------------------------------
#---------------- Coding --------------------------------------

hindi = int(input("Enter Hindi Marks : "))
english = int(input("Enter English Marks : "))
math = int(input("Enter Mathematics Marks : "))
science = int(input("Enter Science Marks : "))
computer = int(input("Enter Computer Marks : "))

average = (hindi + english + math + science + computer)/5

print("Average Marks :", average)

if(hindi < 40 or english < 40 or math < 40 or science < 40 or computer < 40):
    print("Result : FAIL")
else:
    print("Result : PASS")

    if(average >= 75):
        print("Classification : Distinction")
    elif(average >= 60):
        print("Classification : First Division")
    elif(average >= 50):
        print("Classification : Second Division")
    else:
        print("Classification : Pass")

#--------------------------------------------------------------

''' Output :
Average Marks : 82.0
Result : PASS
Classification : Distinction
'''