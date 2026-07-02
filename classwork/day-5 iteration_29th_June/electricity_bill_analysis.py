'''---------- Electricity Bill Analysis ------------------
An electricity department wants to analyze
electricity consumption of N houses.

Accept the monthly units consumed by each house.

Calculate and display:
• Total Units Consumed
• Average Units Consumed
• Highest Consumption
• Lowest Consumption

--------------------------------------------------------------
Sample Input
Enter Number of Houses : 4

House 1 Units : 120
House 2 Units : 180
House 3 Units : 95
House 4 Units : 210

--------------------------------------------------------------
Sample Output
Total Units Consumed : 605
Average Units Consumed : 151.25
Highest Consumption : 210
Lowest Consumption : 95
--------------------------------------------------------------'''
#--------------------------------------------------------------
#---------------- Coding --------------------------------------

# input number of houses
n = int(input("Enter Number of Houses : "))

# validate input
if(n <= 0):
    exit("Number of houses must be positive")

total = 0

for i in range(1, n + 1):

    units = float(input("House " + str(i) + " Units : "))

    total = total + units

    if(i == 1):
        highest = units
        lowest = units
    else:
        if(units > highest):
            highest = units

        if(units < lowest):
            lowest = units

average = total / n

print("Total Units Consumed :", total)
print("Average Units Consumed :", average)
print("Highest Consumption :", highest)
print("Lowest Consumption :", lowest)

#--------------------------------------------------------------

''' Output :
Enter Number of Houses : 4

House 1 Units : 120
House 2 Units : 180
House 3 Units : 95
House 4 Units : 210

Total Units Consumed : 605
Average Units Consumed : 151.25
Highest Consumption : 210
Lowest Consumption : 95
'''