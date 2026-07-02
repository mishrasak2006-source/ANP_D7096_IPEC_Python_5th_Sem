'''---------- ATM Cash Withdrawal ------------------
A customer can withdraw money only if the requested
amount does not exceed the available balance.

Accept the account balance and withdrawal amount.

• If withdrawal amount is less than or equal to balance,
  display:
Transaction Successful

• Otherwise display:
Insufficient Balance
----------------------------------------------------
Sample Input
Enter Account Balance : 5000
Enter Withdrawal Amount : 4500
----------------------------------------------------
Sample Output
Transaction Successful
----------------------------------------------------'''
#----------------------------------------------------
#---------------- Coding ----------------------------

# input of account balance and withdrawal amount
balance = float(input("Enter Account Balance : "))
withdraw = float(input("Enter Withdrawal Amount : "))

# validate input
if(balance < 0 or withdraw <= 0):
    exit("Invalid Amount")

# checking withdrawal
if(withdraw <= balance):
    print("Transaction Successful")
else:
    print("Insufficient Balance")

#----------------------------------------------------

''' Output :
Enter Account Balance : 5000
Enter Withdrawal Amount : 4500
Transaction Successful
'''