browsing_session = []

browsing_session.append(1)  # to add items in the stack
browsing_session.append(2)  # same
browsing_session.append(3)  # same
print((browsing_session))

last = browsing_session.pop()  # delete the item at the top
print(last)

print(browsing_session)

if not browsing_session:  # check if stack is empty or not
    print('Redirect ', browsing_session[-1])  # get the item on the top of the stack
    print("Disable")