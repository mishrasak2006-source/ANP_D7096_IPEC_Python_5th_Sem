'''-----------------Password Strength Checker------------------------------- 
Write a function check_password(password) that checks whether a password is strong.
A password is considered Strong if:
• It contains at least 8 characters.
• It contains at least one uppercase letter.
• It contains at least one lowercase letter.
• It contains at least one digit.
The function should return:
• "Strong Password" or
• "Weak Password"
The main program should accept a password from the user and display the result.

-------------------------------------------------------------------------------------------'''

#------------------------------------------------------------------------------------------

# Function to check password
def check_password(pasword):
    upper = False
    lower = False
    digit = False
    
    # check each character
    for ch in password:
        if ch.isupper():
            upper = 1
        if ch.islower():
            lower = 1
        if ch.isdigit():
            digit = 1

    if len(password) >= 8 and upper == 1 and lower == 1 and digit == 1:
        return "Strong Password"
    else:
        return "Weak Password"
    
    # Main program
    password = input("Enter password: ")
    print(check_password(password))

#----------------------------------------------------------------------

''' Output :

Enter password: Abcd@123
Strong Password

Enter password: abnjuv*87
Weak Password

'''