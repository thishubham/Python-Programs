number = 26
guess = int(input('Enter any number '))

if guess == number:
    print('You guessed it right')
elif guess > number:
    print('You guessed little higher')
else:
    print('You guessed little lower')