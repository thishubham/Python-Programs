# tuple
thistuple = ('apple', 'banana', 'cherry')
print('tuple      ', thistuple, '\n')

# access tuple items
# thistuple = ('apple', 'banana', 'cherry')
print('access tuple item      ', thistuple[2], '\n')

print("Once a tuple is created, you cannot change its values. Tuples are 'unchangeable'.\n")

# loop through a tuple
# thistuple = ('apple', 'banana', 'cherry')
for x in thistuple:
    print('loop through a tuple      ', x, '\n')

# check if item exists
# thistuple = ('apple', 'banana', 'cherry')
if 'apple' in thistuple:
    print("check if item exists      ", "Yes, 'Apple' is in the tuple", '\n')

# tuple length
# thistuple = ('apple', 'banana', 'cherry')
print('tuple length      ', len(thistuple), '\n')

# add items
print('Add Items      . Once a tuple is created, you cannot add items to it. Tuples are \'Unchangable\'')
# thistuple = ('apple', 'banana', 'cherry')
# thistuple[3] = 'Orange'
print(thistuple)

# remove items
print('Remove items      . You cannot remove items in a tuple.\nTuples are unchangable, so you cannot remove items from ir, but you can delete the tuple completely\n')

#delete tuple
# thistuple = ('apple', 'banana', 'cherry')
del thistuple
print('Delete a tuple\n')
# print(thistuple)  this will generate an error

# tuple methods
print('Tuple methods are \n')
print( 'count()	Returns the number of times a specified value occurs in a tuple.\nindex()	Searches the tuple for a specified value and returns the position of where it was found')
