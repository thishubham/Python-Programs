def greet():
    print("This 'def greet()' is a normal function. It just performs a task but doesn't return any kind of value\n\n")


greet()


def get_greetings(name):
    return f'Hey {name}. This "get_greetings(name)" is a function which returns a value as you can see in the code\n' \
        f'With the help of functions like these which returns a value you can store the returned value in a variable\n' \
        f'or use that value in any way you want'


message = get_greetings('Shubham')
print(message)
