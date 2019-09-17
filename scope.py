message = 'n'   # 'message' here is a global variable


def greet():
    message = 'a'    # 'message' here is a local variable
    return message


def send_mail(name):
    print(name)


print(message)