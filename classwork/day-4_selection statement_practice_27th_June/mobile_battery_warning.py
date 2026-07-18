'''---------- Mobile Battery Warning ------------------
A smartphone displays a low battery warning only
when the battery percentage falls below 15%.

Write a Python program to accept the battery
percentage.

If the battery is below 15, display:
Connect Charger Immediately

Otherwise, display nothing.
------------------------------------------------------
Sample Input
Enter Battery Percentage : 10
------------------------------------------------------
Sample Output
Connect Charger Immediately
------------------------------------------------------'''
#------------------------------------------------------
#---------------- Coding ------------------------------

# input of battery percentage
battery = int(input("Enter Battery Percentage : "))

# validate battery percentage
if(battery < 0 or battery > 100):
    exit("Battery percentage must be between 0 and 100")

# checking battery level
if(battery < 15):
    print("Connect Charger Immediately")

#------------------------------------------------------

''' Output :
Enter Battery Percentage : 10
Connect Charger Immediately
'''