'''---------- Electricity Bill Discount ------------------
An electricity provider offers a 10% discount on the total bill amount
if the customer's bill is ₹5000 or more.
Write a Python program that accepts the total bill amount and displays
the final amount to be paid.
----------------------------------------------------------
Sample Input
Enter Electricity Bill Amount: 6200
----------------------------------------------------------
Sample Output
Discount Applied!
Final Bill Amount: ₹5580.0
----------------------------------------------------------
Sample Input
Enter Electricity Bill Amount: 4200
----------------------------------------------------------
Sample Output
No Discount Applied!
Final Bill Amount: ₹4200
----------------------------------------------------------'''
#----------------------------------------------------------
#---------------- Coding ----------------------------------

# input of electricity bill amount
bill = float(input("Enter Electricity Bill Amount : "))

# validate bill amount
if(bill <= 0):
    exit("Bill amount must be positive")

# checking discount eligibility
if(bill >= 5000):
    discount = bill * 0.10
    final_bill = bill - discount
    print("Discount Applied!")
    print("Final Bill Amount : ₹", final_bill)
else:
    print("No Discount Applied!")
    print("Final Bill Amount : ₹", bill)

#----------------------------------------------------------

