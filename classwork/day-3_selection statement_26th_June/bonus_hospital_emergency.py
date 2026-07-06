'''---------- Hospital Emergency Triage System -----------------
A hospital prioritizes patients based on:

• Critical Condition
• Age
• Oxygen Level

Rules:
• Critical Condition -> Immediate Treatment
• Oxygen below 90 -> High Priority
• Age above 65 -> Medium Priority
• Others -> Normal Priority

--------------------------------------------------------------'''
#--------------------------------------------------------------
#---------------- Coding --------------------------------------

critical = input("Critical Condition(Y/N) : ").upper()
age = int(input("Enter Age : "))
oxygen = float(input("Enter Oxygen Level : "))

if(critical == "Y"):
    print("Patient Priority : Immediate Treatment")

elif(oxygen < 90):
    print("Patient Priority : High Priority")

elif(age > 65):
    print("Patient Priority : Medium Priority")
    print("Reason : Senior Citizen")

else:
    print("Patient Priority : Normal Priority")

#--------------------------------------------------------------

''' Output :
Critical Condition(Y/N) : N
Enter Age : 70
Enter Oxygen Level : 94

Patient Priority : Medium Priority
Reason : Senior Citizen
'''