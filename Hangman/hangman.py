import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly choose something from the list
    while '-' in word or ' ' in word: #keeps picking a word until the word does not contain hyphens '-' or spaces ' '
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words) #uses selected word
    word_letters = set(word) #saves letters in the word
    alphabet = set(string.ascii_uppercase) #imports english alphabet in uppercase
    used_letters = set() #tracks what the user has guessed

    lives = 6
    
    #getting user input
    while len(word_letters) > 0 and lives > 0: #while the length of word_letters > 0 and lives > 0, keep iterating
        #letters used
        print ('You have', lives, 'lives left and you have used these letters:', ' '.join(used_letters))

        # show current word with correct guesses filled in and hyphen '-' filling blanks
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters: #if user_letter is valid in the alphabet
            used_letters.add(user_letter) #then add user_letter to used_letter list
            if user_letter in word_letters: #if the user_letter is in the selected word
                word_letters.remove(user_letter) #then remove user_letter from word_letters

            else:
                lives = lives - 1 #removes 1 life for incorrect guess
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You already guessed that letter. Try a different one!')

        else:
            print('Invalid character, try again.')
    #arrive here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print('Hangman is dead, sorry. The word was', word)
    else:
        print('You have guessed the word', word, '! Congrats!')

hangman()