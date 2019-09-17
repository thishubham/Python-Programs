def increment(number, by=9):  # we can also declare "Optional Parameter" value to a parameter in the function definition.
    return number + by        # so in case we do not pass a value while calling then it takes default value


print(increment(number=8))  # in the function if there are many arguments then we
print(increment(10, 2))     # can assign parameter names while calling the fucntion
