'''---------- Shopping Cart Billing System ------------------
A supermarket allows a customer to purchase
multiple products.

The customer first enters the number of products.

For each product, enter:
• Product Name
• Quantity
• Price per Unit

Finally display:
• Individual Product Cost
• Total Bill Amount
• Most Expensive Product
• Cheapest Product
• Average Product Cost

------------------------------------------------------------
Sample Input
Enter Number of Products : 3

Product Name : Pen
Quantity : 10
Price per Unit : 20

Product Name : Book
Quantity : 2
Price per Unit : 250

Product Name : Bag
Quantity : 1
Price per Unit : 800

------------------------------------------------------------
Sample Output
Pen Cost : ₹200
Book Cost : ₹500
Bag Cost : ₹800

Total Bill Amount : ₹1500
Most Expensive Product : Bag
Cheapest Product : Pen
Average Product Cost : ₹500.0
------------------------------------------------------------'''
#------------------------------------------------------------
#---------------- Coding ------------------------------------

# input number of products
n = int(input("Enter Number of Products : "))

# validate input
if(n <= 0):
    exit("Number of products must be positive")

total_bill = 0

for i in range(1, n + 1):

    name = input("Product Name : ")
    quantity = int(input("Quantity : "))
    price = float(input("Price per Unit : "))

    cost = quantity * price

    print(name, "Cost : ₹", cost)

    total_bill += cost

    if(i == 1):
        highest_cost = cost
        lowest_cost = cost
        expensive_product = name
        cheapest_product = name

    else:
        if(cost > highest_cost):
            highest_cost = cost
            expensive_product = name

        if(cost < lowest_cost):
            lowest_cost = cost
            cheapest_product = name

average = total_bill / n

print("Total Bill Amount : ₹", total_bill)
print("Most Expensive Product :", expensive_product)
print("Cheapest Product :", cheapest_product)
print("Average Product Cost : ₹", average)

#------------------------------------------------------------

''' Output :
Enter Number of Products : 3

Product Name : Pen
Quantity : 10
Price per Unit : 20

Pen Cost : ₹ 200

Product Name : Book
Quantity : 2
Price per Unit : 250

Book Cost : ₹ 500

Product Name : Bag
Quantity : 1
Price per Unit : 800

Bag Cost : ₹ 800

Total Bill Amount : ₹ 1500
Most Expensive Product : Bag
Cheapest Product : Pen
Average Product Cost : ₹ 500.0
'''