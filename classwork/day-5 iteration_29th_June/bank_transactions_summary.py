'''---------- Bank Transaction Summary ------------------
A customer keeps entering transaction amounts.

Positive numbers indicate deposits.
Negative numbers indicate withdrawals.
The customer enters 0 to finish.

Display:
• Total Deposit
• Total Withdrawal
• Final Balance

--------------------------------------------------------
Sample Output

Enter Transaction Amount : 5000
Enter Transaction Amount : -1500
Enter Transaction Amount : 2000
Enter Transaction Amount : -500
Enter Transaction Amount : 0

Total Deposit : ₹7000
Total Withdrawal : ₹2000
Final Balance : ₹5000
--------------------------------------------------------'''
#--------------------------------------------------------
#---------------- Coding --------------------------------

# initialize variables
deposit = 0
withdrawal = 0
balance = 0

n = int(input("Enter Number of Transactions : "))

deposit = 0
withdrawal = 0
balance = 0

for i in range(n):

    amount = float(input("Enter Transaction Amount : "))

    if(amount > 0):
        deposit += amount
    else:
        withdrawal += abs(amount)

    balance += amount

print("Total Deposit :", deposit)
print("Total Withdrawal :", withdrawal)
print("Final Balance :", balance)

#--------------------------------------------------------

''' Output :
Enter Transaction Amount : 5000
Enter Transaction Amount : -1500
Enter Transaction Amount : 2000
Enter Transaction Amount : -500
Enter Transaction Amount : 0

Total Deposit : ₹7000
Total Withdrawal : ₹2000
Final Balance : ₹5000
'''