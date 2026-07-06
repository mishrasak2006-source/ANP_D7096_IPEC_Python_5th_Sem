'''---------- Login System with Maximum Attempts ------------------
A system allows only three login attempts.

Correct Username : admin
Correct Password : python123

If the credentials are correct, display:
Login Successful

Otherwise, after three unsuccessful attempts,
display:
Account Locked

---------------------------------------------------------------
Sample Output

Attempt 1
Username : admin
Password : abc
Invalid Credentials

Attempt 2
Username : admin
Password : python123
Login Successful

---------------------------------------------------------------'''
#---------------------------------------------------------------
#---------------- Coding ---------------------------------------

for i in range(1, 4):

    print("Attempt", i)

    username = input("Username : ")
    password = input("Password : ")

    if(username == "admin" and password == "python123"):
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
else:
    print("Account Locked")

#---------------------------------------------------------------

''' Output :

Attempt 1
Username : admin
Password : abc
Invalid Credentials

Attempt 2
Username : admin
Password : python123
Login Successful
'''