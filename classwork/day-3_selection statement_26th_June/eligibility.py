'''---------- Voting Eligibility ------------------
A person is eligible to vote only if they are
18 years of age or older.
Write a Python program that accepts the age of a person
and determines whether they are eligible to vote.
---------------------------------------------------
Sample Input
Enter Your Age: 20
---------------------------------------------------
Sample Output
You are eligible to vote.
---------------------------------------------------
Sample Input
Enter Your Age: 16
---------------------------------------------------
Sample Output
You are not eligible to vote.
---------------------------------------------------'''
#---------------------------------------------------
#---------------- Coding ---------------------------

# input of age from user
age = int(input("Enter Your Age : "))

# validate age
if(age <= 0):
    exit("Age must be positive")

# checking voting eligibility
if(age >= 18):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#---------------------------------------------------

''' Output :
Enter Your Age : 20
You are eligible to vote.
'''