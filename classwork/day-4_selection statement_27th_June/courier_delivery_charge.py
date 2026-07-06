'''---------- Courier Delivery Charge ------------------
A courier company calculates delivery charges
based on the package weight.

• Weight up to 2 kg           -> ₹50
• Weight greater than 2 kg
  and up to 5 kg              -> ₹100
• Weight greater than 5 kg    -> ₹180

Write a Python program to display the delivery
charge.
--------------------------------------------------------
Sample Input
Enter Package Weight : 4
--------------------------------------------------------
Sample Output
Delivery Charge = ₹100
--------------------------------------------------------'''
#--------------------------------------------------------
#---------------- Coding --------------------------------

# input of package weight
weight = float(input("Enter Package Weight : "))

# validate weight
if(weight <= 0):
    exit("Weight must be positive")

# calculating delivery charge
if(weight <= 2):
    charge = 50
elif(weight <= 5):
    charge = 100
else:
    charge = 180

print("Delivery Charge = ₹", charge)

#--------------------------------------------------------

''' Output :
Enter Package Weight : 4
Delivery Charge = ₹ 100
'''
