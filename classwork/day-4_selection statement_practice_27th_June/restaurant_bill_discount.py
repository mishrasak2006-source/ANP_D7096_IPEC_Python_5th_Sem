'''---------- Restaurant Bill Discount ------------------
A restaurant offers discounts based on the
total bill amount.

• Bill below ₹1000 -> No Discount
• ₹1000 to ₹2999 -> 10% Discount
• ₹3000 or more -> 20% Discount

Write a Python program to determine the
applicable discount.
--------------------------------------------------------
Sample Input
Enter Bill Amount : 3200
--------------------------------------------------------
Sample Output
20% Discount Applied
--------------------------------------------------------'''
#--------------------------------------------------------
#---------------- Coding --------------------------------

# input of bill amount
bill = float(input("Enter Bill Amount : "))

# validate bill amount
if(bill <= 0):
    exit("Bill amount must be positive")

# checking discount
if(bill < 1000):
    print("No Discount Applied")
elif(bill < 3000):
    print("10% Discount Applied")
else:
    print("20% Discount Applied")

#--------------------------------------------------------

''' Output :
Enter Bill Amount : 3200
20% Discount Applied
'''