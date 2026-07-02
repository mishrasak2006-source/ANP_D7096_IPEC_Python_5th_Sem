'''---------- Internet Speed Rating ------------------
An Internet Service Provider categorizes connection
quality based on download speed.

• Less than 25 Mbps -> Slow
• 25–99 Mbps -> Good
• 100 Mbps or above -> Excellent

Write a Python program to display the
connection quality.
------------------------------------------------------
Sample Input
Enter Internet Speed : 120
------------------------------------------------------
Sample Output
Excellent Connection
------------------------------------------------------'''
#------------------------------------------------------
#---------------- Coding ------------------------------

# input of internet speed
speed = float(input("Enter Internet Speed (Mbps) : "))

# validate speed
if(speed < 0):
    exit("Speed cannot be negative")

# checking connection quality
if(speed < 25):
    print("Slow Connection")
elif(speed < 100):
    print("Good Connection")
else:
    print("Excellent Connection")

#------------------------------------------------------

''' Output :
Enter Internet Speed (Mbps) : 120
Excellent Connection
'''