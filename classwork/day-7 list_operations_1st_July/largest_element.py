# Input number of elements
n = int(input("Enter Number of Elements: "))

# Create an empty list
lst = []

# Input elements
for i in range(n):
    num = int(input("Enter Element: "))
    lst.append(num)

# Assume first element is the largest
largest = lst[0]

# Compare every element
for i in lst:
    if i > largest:
        largest = i

# Display largest element
print("Largest Element:", largest)