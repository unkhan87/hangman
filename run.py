# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from hangman_art import logo
from words import words_list


def welcome_msg():
    """
    Welcome message for the user.
    """
    print(logo)
    user_name = input('Please enter your name: \n')
    print(
        f'Hi {user_name}, Welcome to Hangman!\n'
    )

    view_instructions = input(
        'Please type 1 to see the instructions, ' 'or 2 to start the the game!:\n' 
    )
    
    # This is to make sure the input is valid
    while view_instructions != "1" and view_instructions != "2":
        view_instructions = input(
            'Invalid input, Please type 1 to see the instructions or 2 to start the game'
        )
    
    # Take user to choice they made on the first step
    if view_instructions == "1":
        instructions()
    else:
        get_word()
    
def instructions():
    """
    Show instructions to the user and confirm if the user is ready to play
    """
    print(
        'Instructions:\n\n To play hangman you will need to guess your word letter by letter.\n\n1. Start guessing '
        'the letter and hit enter.\n2. If your letter is correct one of the blank space will get populated.\n3. If '
        'you gussed an incorrect letter you will get a strike and a section of a hangman will appear.\n4. You have got '
        '6 tries to guess the word.\n'
    )

    # Confirm if the user is ready to play the game
    print("Are you ready to play Hangman?")
    play = input('Please type 1 for yes and 2 for no:\n')
    # this is to check if user input invalid number
    while play != "1" and play != "2":
        play = input(
            '\nInvalid Input, if you are ready to play '
            'enter 1 if not enter 2:\n'
        )

    get_word()

def get_word():
    word = random.choice(words_list)
    play(word.upper())

def play(word):
    """
    get random words from the words list, and ask the user to guess the words 
    """
    # Initialize variables
    # Blanks for each letter in the word
    current_guess = "_ " * len(word)
    word_guessed = False
    tries = 6
    # used letters tracker
    used_letters=[]
    # Main Loop
    print("Let's Play Hangman!")
    while not word_guessed and tries > 0:
        print(display_hangman(tries))
        print(current_guess)
        # Promt the user to enter the letter
        guess = input("Please guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            # Checks if the letter the user has already been used
            if guess in used_letters:
                print("You already guessed that letter", guess)
                continue
            # prints statement with a guess letter if it wrong
            elif guess not in word:
                print(guess, "is not in word, try again")
                tries -= 1
                # Add new guessed letter to list of guessed letters
                used_letters.append(guess)
                continue
            # If user made a correct letter guess
            else:
                print("You have guessed the correct letter!", guess)
                used_letters.append(guess)
                current_guess = " "
                for letter in word:
                    if letter in used_letters:
                        current_guess = current_guess + letter + " "
                    else:    
                        current_guess = current_guess + "_ "

        else:
            print("Invalid Input")
            continue

    if tries == 0:
        print(display_hangman(tries))
        print("You are out of tries")
        print("The word was", word,"!\n")
        play_again()
    else:
        print("Congratulations!\nYou "
        "guessed the word", word,"! You Win!")
        play_again()


def play_again():
    """
    Ask user if they like to play the game again
    """
    play_again_option = input("Would you like to play the game again? \n"
    "Type 1 for Yes or 2 for No:\n")

    # Making sure the user input is valid
    while play_again_option != "1" and play_again_option != "2":
        play_again_option = input("Invalid Input!\n"
        "Please press 1 to play again and if not please press 2: \n")

    # Take user to the relevant section of the game
    if play_again_option == "1":
        get_word()
    else:
        print("Thanks for playing Hangman. I hope you enjoyed it, Goodbye\n")
        print("If you like to play again, refresh the page by clicking "
        "'run program option' at the top." )

def display_hangman(tries):
    stages = ['''
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    ''', '''
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    ''', '''
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    ''', '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    ''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    ''', '''
    +---+
    |   |
        |
        |
        |
        |
    =========
    ''']
    return stages[tries]
        

welcome_msg()



