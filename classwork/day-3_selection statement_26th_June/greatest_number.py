'''Program to find out the greatest number between two number'''
#input of first number from user
num1 = int(input("Enter first number: "))
#-------------------------------------------
#input of second number from user
num2 = int(input("Enter second number: "))
#--------------------------------------------
print("---------------------------")
#finding the greatest
if(num1 > num2):
    print(num1,"is greater than",num2)
elif(num2 > num1):
    print(num2,"is greater than",num1)
else:
    print(num1,"is equal to",num2)
#---------------------------------------

'''Output:
