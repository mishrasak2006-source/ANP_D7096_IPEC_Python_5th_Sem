'''---------- Parking Entry Validation ------------------
Only vehicles having a valid parking pass are
allowed to enter a private parking area.

Accept input as:
• 1 -> Valid Pass
• 0 -> No Pass

If the input is 1, display:
Entry Allowed

Otherwise display:
Entry Denied
--------------------------------------------------------
Sample Input
Enter Parking Pass (1/0) : 0
--------------------------------------------------------
Sample Output
Entry Denied
--------------------------------------------------------'''
#--------------------------------------------------------
#---------------- Coding --------------------------------

# input of parking pass
pass_status = int(input("Enter Parking Pass (1/0) : "))

# validate input
if(pass_status != 0 and pass_status != 1):
    exit("Invalid Input")

# checking parking entry
if(pass_status == 1):
    print("Entry Allowed")
else:
    print("Entry Denied")

#--------------------------------------------------------

''' Output :
Enter Parking Pass (1/0) : 0
Entry Denied
'''