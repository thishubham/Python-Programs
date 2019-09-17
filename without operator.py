mark1 = int(input("Enter English Score "))
mark2 = int(input("Enter Maths Score "))
mark3 = int(input("Enter Python Score "))

message = "Pass" if mark1>30 and mark2>30 and mark3>30 else "Fail"

print(message)