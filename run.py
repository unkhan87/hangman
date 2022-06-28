# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from words import words_list


def welcome_msg():
    """
    Welcome message for the user.
    """
    print(
        'Welcome to Hangman!\n'
    )

    view_instructions = input(
        'Please type 1 to see the instructions, ' 'or 2 to start the the game!:\n' 
    )
    
    #This is to make sure the input is valid
    while view_instructions != "1" and view_instructions != "2":
        view_instructions = input(
            'Invalid input, Please type 1 to see the instructions or 2 to start the game'
        )
    
    #Take user to choice they made on the first step
    if view_instructions == "1":
        instructions()
    else:
        get_word()
    
def instructions():
    """
    Show instructions to the user
    """
    print(
        'Instructions:\n\n To play hangman you will need to guess your word letter by letter.\n\n1. Start guessing'
        'the letter and hit enter.\n2. If your letter is correct it one of the blank space will get populated.\n3. If'
        'you gussed an incorrect letter you will get a strike and a section of a hangman will appear.\n4. You have got'
        '6 tries to guess the word.'
    )
welcome_msg()