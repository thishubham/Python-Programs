numbers = [1, 1, 3, 5, 3, 2]  # It has repeated values
first = set(numbers)  # Set removes the duplicate values
second = {1, 4}

print(first | second)  # "|" (vertical bar) stands for the Union
print(first & second)  # "&" Intersection
print(first - second)  # Difference
print(first ^ second)  # Symmetric Difference

