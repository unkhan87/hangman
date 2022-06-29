# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from words import words_list


def welcome_msg():
    """
    Welcome message for the user.
    """
    user_name = input('Please enter your name: \n')
    print(
        f'Hi {user_name}, Welcome to Hangman!\n'
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
    Show instructions to the user and confirm if the user is ready to play
    """
    print(
        'Instructions:\n\n To play hangman you will need to guess your word letter by letter.\n\n1. Start guessing'
        'the letter and hit enter.\n2. If your letter is correct it one of the blank space will get populated.\n3. If'
        'you gussed an incorrect letter you will get a strike and a section of a hangman will appear.\n4. You have got'
        '6 tries to guess the word.\n'
    )

    #Confirm if the user is ready to play the game
    print("Are you ready to play Hangman?")
    play = input('Please type 1 for yes and 2 for no:\n')
    #this is to check if user input invalid number
    while play != "1" and play != "2":
        play = input(
            '/nInvalid Input, if you are ready to play '
            'enter 1 if not enter 2:/n'
        )

welcome_msg()