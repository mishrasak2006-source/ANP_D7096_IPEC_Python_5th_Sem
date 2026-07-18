'''---------- Secure Vault Access ------------------
A digital vault can only be opened if the user
enters the correct security code.

Write a Python program that accepts the entered
security code.

If the entered code is 7890, display:
Access Granted to the Vault.

Otherwise, do nothing.
----------------------------------------------------
Sample Input
Enter Security Code : 7890
----------------------------------------------------
Sample Output
Access Granted to the Vault.
----------------------------------------------------'''
#----------------------------------------------------

# input of security code
code = int(input("Enter Security Code : "))

# checking security code
if(code == 7890):
    print("Access Granted to the Vault.")

#----------------------------------------------------

''' Output :
Enter Security Code : 7890
Access Granted to the Vault.
'''