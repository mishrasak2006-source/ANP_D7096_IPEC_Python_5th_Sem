'''---------- Parking Fee Waiver --------------------------
A shopping mall waives the parking fee if the customer has
made purchases worth ₹2000 or more.
Otherwise, the parking fee is ₹100.
----------------------------------------------------------
Sample Input
Enter Purchase Amount: 2500
----------------------------------------------------------
Sample Output
Parking Fee Waived!
Parking Fee: ₹0
----------------------------------------------------------
Sample Input
Enter Purchase Amount: 1500
----------------------------------------------------------
Sample Output
Parking Fee Applicable!
Parking Fee: ₹100
----------------------------------------------------------'''
#----------------------------------------------------------
#---------------- Coding ----------------------------------

# input of purchase amount
purchase = float(input("Enter Purchase Amount : "))

# validate purchase amount
if(purchase <= 0):
    exit("Purchase amount must be positive")

# checking parking fee
if(purchase >= 2000):
    print("Parking Fee Waived!")
    print("Parking Fee : ₹0")
else:
    print("Parking Fee Applicable!")
    print("Parking Fee : ₹100")

#----------------------------------------------------------

''' Output :
Enter Purchase Amount : 2500
Parking Fee Waived!
Parking Fee : ₹0
'''