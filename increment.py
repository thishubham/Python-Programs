x = int(input("Enter a number to see next 5 consecutive numbers "))

print("Next 5 numbers are ")

for number in range(5):
    print(x + 1)
    x += 1
