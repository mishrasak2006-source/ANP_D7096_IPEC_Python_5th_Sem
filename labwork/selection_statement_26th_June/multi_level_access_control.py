'''---------- Multi-Level Access Control System ----------------
Assign access levels based on:

Roles:
• Admin
• Manager
• Employee
• Guest

Conditions:
• Admin + Security Clearance >=5 -> Full Access
• Manager + Experience >5 Years -> Department Access
• Employee + Experience >2 Years -> Limited Access
• Guest -> Read Only Access
• Inactive Account -> No Access

--------------------------------------------------------------'''
#--------------------------------------------------------------
#---------------- Coding --------------------------------------

role = input("Enter Role : ").lower()
status = input("Enter Account Status(Active/Inactive) : ").lower()

if(status == "inactive"):
    print("Access Level : NO ACCESS")

else:

    if(role == "admin"):
        clearance = int(input("Enter Security Clearance : "))
        if(clearance >= 5):
            print("Access Level : FULL ACCESS")
        else:
            print("Access Level : LIMITED ACCESS")

    elif(role == "manager"):
        experience = int(input("Enter Experience (Years) : "))
        if(experience > 5):
            print("Access Level : DEPARTMENT ACCESS")
        else:
            print("Access Level : LIMITED ACCESS")

    elif(role == "employee"):
        experience = int(input("Enter Experience (Years) : "))
        if(experience > 2):
            print("Access Level : LIMITED ACCESS")
        else:
            print("Access Level : BASIC ACCESS")

    else:
        print("Access Level : READ ONLY ACCESS")

#--------------------------------------------------------------

''' Output :
Role : Admin
Security Clearance : 6
Account Status : Active

Access Level : FULL ACCESS
'''