"""Number Guessing Game
Computer generates a random number between 1-100.
The player guesses until they find the number.
Give hints (“too high”, “too low”)."""

import random

com_guess = random.randrange(1, 101)
user_guess = 0
high = 100
low = 1

while com_guess != user_guess:
    user_input = input('Enter Your guess:')
    
    try:
        user_guess = int(user_input)
    except ValueError:
        print(ValueError)
        
        
    if user_guess < 1 or user_guess > 100:
        print("You should Enter value between 1 and 100:")
    else:
        pass
      
    if user_guess >= 1 and user_guess <= 100:   
        if user_guess > com_guess:
            print(user_guess, 'is too high!')
            high = user_guess
        else:
            print(user_guess, 'is too low!')
            low = user_guess

    
        print(f'Your Previous high: {high} and previous low: {low}')


print("You guessed it right!: ", user_guess)


