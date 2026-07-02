'''---------- Password Strength Checker ------------------
A website requires users to create a password
having at least 8 characters.

Keep asking the user to enter a password until
the entered password satisfies the minimum
length requirement.
----------------------------------------------------------
Sample Output
Enter Password : hello
Password too short.
Enter Password : python@123
Password Accepted.
----------------------------------------------------------'''
#----------------------------------------------------------
#---------------- Coding ----------------------------------

for i in range(1, 4):

    password = input("Enter Password : ")

    if(len(password) >= 8):
        print("Password Accepted.")
        break
    else:
        print("Password too short.")

#----------------------------------------------------------

''' Output :
Enter Password : hello
Password too short.
Enter Password : python@123
Password Accepted.
'''