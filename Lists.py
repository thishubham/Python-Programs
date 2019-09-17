# In list we can have objects of any type

letters = ['a', 'b', 'c']
print(letters)

matrix = [[0, 1], [2, 3]]  # list of lists
print(matrix)

zeros = [0] * 5
print(zeros)

combined = zeros + letters
print(combined)

numbers = list(range(20))
print(numbers)

chars = list('hello world')
print(chars)

print(len(chars))