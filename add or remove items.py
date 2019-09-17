letters = ['a', 'b', 'c']

# Add
letters.append('d')  # add value at the end if the list
letters.insert(0, '-')  # insert at a particular index in the list
print(letters)

# Remove
letters.pop(0)  # by default removes last item from the list
letters.remove('d')  # if we don't know the index then we can use this. If multiple characters are present then it'll remove 1st one
# del letters[0:3]  # delete can remove from a range of index
letters.clear()  # removes all elements from the list
print(letters)