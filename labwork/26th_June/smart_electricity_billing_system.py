'''---------- Smart Electricity Billing System ----------------
Calculate electricity bill using:

0-100 Units      -> ₹5 per unit
101-300 Units    -> ₹7 per unit
Above 300 Units  -> ₹10 per unit

Additional Rules:
• Commercial consumers pay 20% extra.
• Bills above ₹5000 attract 5% surcharge.
• Senior citizens receive 10% discount.

--------------------------------------------------------------
Sample Input
Units Consumed : 450
Consumer Type (Residential/Commercial) : Commercial
Senior Citizen(Y/N) : Y
--------------------------------------------------------------
Sample Output
Base Bill : ₹4500
Commercial Charge : ₹900
Surcharge : ₹270
Senior Citizen Discount : ₹567
Final Bill Amount : ₹5103
--------------------------------------------------------------'''
#--------------------------------------------------------------
#---------------- Coding --------------------------------------

units = int(input("Enter Units Consumed : "))
ctype = input("Enter Consumer Type(Residential/Commercial) : ").lower()
senior = input("Senior Citizen(Y/N) : ").upper()

if(units <= 100):
    bill = units * 5
elif(units <= 300):
    bill = units * 7
else:
    bill = units * 10

print("Base Bill : ₹", bill)

commercial = 0
surcharge = 0
discount = 0

if(ctype == "commercial"):
    commercial = bill * 0.20
    bill = bill + commercial
    print("Commercial Charge : ₹", commercial)

if(bill > 5000):
    surcharge = bill * 0.05
    bill = bill + surcharge
    print("Surcharge : ₹", surcharge)

if(senior == "Y"):
    discount = bill * 0.10
    bill = bill - discount
    print("Senior Citizen Discount : ₹", discount)

print("Final Bill Amount : ₹", bill)

#--------------------------------------------------------------

''' Output :
Base Bill : ₹4500
Commercial Charge : ₹900
Surcharge : ₹270
Senior Citizen Discount : ₹567
Final Bill Amount : ₹5103
'''