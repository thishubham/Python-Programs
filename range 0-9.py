no = int(input("Enter a number between 0 and 9 "))

if no == 9:
    message = "Nine"
elif no == 8:
    message = "Eight"
elif no == 7:
    message = "Seven"
elif no == 6:
    message = "Six"
else:
    message = "Out of Range"

print(message)