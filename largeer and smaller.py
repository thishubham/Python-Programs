'''
a = int(input("Enter the first number "))
b = int(input("Enter the second number "))
c = int(input("Enter the third number "))
d = int(input("Enter the fourth number "))

print("\nLARGEST NUMBER IS")
if a > b > c > d:
    print(a," is the largest number")
elif b > c > d:
    print(b, "is the largest number")
elif c > d:
    print(c," is the largest number")
else:
    print(d," is the largest number")

print("\nSMALLEST NUMBER IS")
if a < b < c < d:
    print(a, "is the smallest number")
elif b < c < d:
    print(b, "is the smallest number")
elif c < d:
    print(c, "is the smallest number")
else:
    print(d, "is the smallest number")
'''

lst = []
num = int(input("How many numbers "))

for n in range(num):
    numbers = int(input("Enter the number "))
    lst.append(numbers)

print("Maximum number is ", max(lst), "\nMinimum number is ",min(lst))