from array import array

numbers = array("i", [1, 2, 3])

numbers.append(5)
print(numbers)
numbers.pop()
print(numbers)
numbers.remove(1)
print(numbers)