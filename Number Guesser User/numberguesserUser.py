import random

def computer_guess(x):
    low = 1
    high = x
    feedback = input(f'Want to play a game? Yes (Y) or No (N)?').lower()
    if feedback == 'y':
        while feedback != 'c':
            guess = random.randint(low, high)
            feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()
            if feedback == 'h':
                high = guess - 1
            elif feedback == 'l':
                low = guess + 1
        print(f'Yay! The computer guessed your number {guess}, correctly!')
    elif feedback == 'n':
        print('Thats alright. Maybe next time.')

computer_guess(10)