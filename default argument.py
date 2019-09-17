def increment(number, by=3):     # here 'by' is the default argument beacuse we gave it a default value so that in case while calling
    return number + by           # this function if we do not give a value to 'by' parameter then compiler will that this default value


print(increment(5, 2))              # here if we don't pass 2nd argument then default value will be taken
