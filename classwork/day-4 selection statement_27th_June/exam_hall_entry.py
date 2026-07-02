'''---------- Exam Hall Entry ------------------
Students are allowed to enter the examination
hall only if they are carrying their admit card.

Accept input as:
• 1 -> Admit Card Available
• 0 -> Admit Card Not Available

If the input is 1, display:
Enter Examination Hall

Otherwise, do not display anything.
------------------------------------------------
Sample Input
Enter Admit Card Status (1/0) : 1
------------------------------------------------
Sample Output
Enter Examination Hall
------------------------------------------------'''
#------------------------------------------------
#---------------- Coding ------------------------

# input of admit card status
admit = int(input("Enter Admit Card Status (1/0) : "))

# validate input
if(admit != 0 and admit != 1):
    exit("Invalid Input")

# checking admit card
if(admit == 1):
    print("Enter Examination Hall")

#------------------------------------------------

''' Output :
Enter Admit Card Status (1/0) : 1
Enter Examination Hall
'''