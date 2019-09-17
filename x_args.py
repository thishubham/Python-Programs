def multiply(*numbers):
    print("'*numbers' means that the function can take multiple arguments")
    total = 1
    for number in numbers:
        print(number)
        # total *= number
    # return total


print(multiply(2, 3, 4, 5))
print('At the end of the execution you can see "None"\n' \
      'Unless you specifically return a value. It is going to return "None"\n' \
      'None is the return value of the multiply function')