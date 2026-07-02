'''---------- Count Prime Numbers in a Range ------------------
Accept two integers representing the starting and
ending values of a range.

Display all prime numbers within the range and
finally display the total number of prime numbers
found.

--------------------------------------------------------------
Sample Input
Enter Starting Number : 10
Enter Ending Number : 30
--------------------------------------------------------------
Sample Output
Prime Numbers :
11
13
17
19
23
29
Total Prime Numbers = 6
--------------------------------------------------------------'''
#--------------------------------------------------------------
#---------------- Coding --------------------------------------

# input of range
start = int(input("Enter Starting Number : "))
end = int(input("Enter Ending Number : "))

# validate range
if(start > end):
    exit("Invalid Range")

count = 0

print("Prime Numbers :")

for num in range(start, end + 1):

    if(num > 1):
        prime = True

        for i in range(2, num):
            if(num % i == 0):
                prime = False
                break

        if(prime):
            print(num)
            count += 1

print("Total Prime Numbers =", count)

#--------------------------------------------------------------

''' Output :
Enter Starting Number : 10
Enter Ending Number : 30

Prime Numbers :
11
13
17
19
23
29
Total Prime Numbers = 6
'''