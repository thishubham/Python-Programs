print("Swapping two numbers")

x = int(input("Enter the first number "))
y = int(input("Enter the second number "))

print("Before swapping numbers are 1st ", x ," 2nd ", y)

x = x + y
y = x - y
x = x - y

print("After swapping numbers are 1st ", x  ," 2nd ", y)