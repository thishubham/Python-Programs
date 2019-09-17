# WE CAN SEPARATELY ASSIGN LISTS' OBJECTS TO DIFFERENT VARIABLES

numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers)

# first, second, third, fourth = numbers
# NUMBER OF VARIABLES ON THE LEFT SIDE OF ASSIGNMENT OPERATOR SHOULD BE EQUAL TO THE NUMBER OF ITEMS IN THE LIST

# 6th line and 10, 11, 12 lines have same meaning
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

first, second, *others = numbers  # 1st and 2nd item of list will be in separate variables and all other items will be in "other" list
# WE FIRST UNPACKED ITEMS INTO 'FIRST' AND 'SECOND' VARIABLES THEN ALSO PACKED ALL OTHER ITEMS IN 'OTHERS' LIST

print(first, second)
print(others)

# if we want to include 1st and last item in variables then we can write "FIRST, *OTHERS, LAST = NUMBERS"
