number = 26
running = True

while running:  # runs until 'running' becomes 'false'
    guess = int(input('Enter any number '))

    if guess == number:
        print('You guessed it right')
        running = False  # 'running' changes it's value to false and while gets executed
    elif guess > number:
        print('You guessed little higher')
    else:
        print('You guessed little lower')
else:
    print('While loop is over')

print('Executed')