# list
list = ['apple', 'banana', 'cherry']
print('list      ', list, '\n')

# access items
# list = ['apple', 'banana', 'cherry']
print('access item      ', list[1], '\n')

# change item value
# list = ['apple', 'banana', 'cherry']
list[1] = 'blackcurrent'
print('change item value      ', list, '\n')

# loop through a list
# list = ['apple', 'blackcurrent', 'cherry']
for x in list:
    print('loop through a list      ', x, '\n')

# check if the item exists
# list = ['apple', 'blackcurrent', 'cherry']
if 'apple' in list:
    print('check if item exists      Yes, Apple is in the list', '\n')

# list lenght
# list = ['apple', 'blackcurrent', 'cherry']
print('list length      ', len(list), '\n')

# add items
# list = ['apple', 'blackcurrent', 'cherry']
list.append('Orange')
print('add items      ', list, '\n')

# To add an item at the specified index, use the insert() method:
# list = ['apple', 'blackcurrent', 'cherry', 'orange']
list.insert(1, 'Mango')
print('add at specific index      ', list, '\n')

# remove item
# list = ['apple', 'Mango', 'blackcurrent', 'cherry', 'orange']
list.remove('blackcurrent')
print('remove item      ', list, '\n')

# pop() removes the specified index
# list = ['apple', 'Mango', 'cherry', 'Orange']
list.pop(0)
print('pop() removes from a specific index      ', list, '\n')


# pop() removes last item if index not specified
# list = ['Mango', 'cherry', 'Orange']
list.pop()
print('pop() removes last item if index not specified      ', list, '\n')

# del keyword removes specified index
# list = ['Mango', 'Cherry']
del list[0]
print('del keyword removes specified index      ', list, '\n')

# del keyword can also delete the list completely:
# list = ['Cherry']
# del list
print("'Del' Keyword can also delete the entire list", '\n')

# copy a list
# list = ['Cherry']
list_1 = list.copy()
print('List is copied. This is not \"list\", this is \"list_1\"      ', list_1, '\n')

# The clear() method empties the list:
# list = ['Cherry']
list.clear()
print("'clear' method empties the list      ", list, '\n')

print('List Methods')
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list