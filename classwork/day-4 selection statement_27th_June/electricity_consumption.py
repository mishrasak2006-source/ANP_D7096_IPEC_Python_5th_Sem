'''---------- Electricity Consumption Category ------------------
An electricity department categorizes households
based on monthly electricity consumption.

• Up to 100 units -> Low Consumption
• 101–300 units -> Moderate Consumption
• Above 300 units -> High Consumption

Write a Python program to display the
consumption category.
---------------------------------------------------------------
Sample Input
Enter Electricity Units : 245
---------------------------------------------------------------
Sample Output
Moderate Consumption
---------------------------------------------------------------'''
#---------------------------------------------------------------
#---------------- Coding ---------------------------------------

# input of electricity units
units = int(input("Enter Electricity Units : "))

# validate units
if(units < 0):
    exit("Units cannot be negative")

# checking consumption category
if(units <= 100):
    print("Low Consumption")
elif(units <= 300):
    print("Moderate Consumption")
else:
    print("High Consumption")

#---------------------------------------------------------------

''' Output :
Enter Electricity Units : 245
Moderate Consumption
'''