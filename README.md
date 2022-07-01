# Hangman

Hangman is a guessing game and is usually played by two or more people, where one player thinks of a word while the other players guess what the word is by guessing one letter at a time until the whole word is revealed or they run out of tries.
The game is usually played with a Paper-and-pencil however I decided to create electronic version of the game that you can play against the computer rather than playing against another person.
I've used python programming language to program this game. Number of different functions have been created in order to achieve different tasks for this game.

## How To Play

In this version of Hangman the system generates a random word and display it to the user however instead of words blank lines get displayed on the users screen. Users have got six attempts to guess if they cannot do it in the given attempts they lose and get asked to if the user wants to play again however if they do guess a word then they win the game.

## Objectives

- Is easy to navigate. 
    - Was this achieved?
        - Yes
    - How was this achieved?
        - By creating a user friendly process for the game by giving clear and concise options to the user like Option 1 for 'Yes' and Option 2 for 'No'.  
                        
 - I want the game to run in a smooth loop to allow the user to keep playing as many times as they'd like to. 
    - Was this achieved?
        - Yes
    - How was this achieved?
        - The game give users the option if they like play again or if they would like to quit. Again option 1 for 'Yes' and option 2 for 'No'.

- To make it clear to the user how many tries they have left until the game is over.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - When the user gets a guess wrong the number of tries left is printed and each round if they get the answer right or wrong it will print out the traditional hangman image that shows how many tries the user has left in the game.

- I want to give the user a choice of how hard they would like to challenge themselves.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - To achieve this I created two lists, one with shorter words making them easier to guess and one with longer words making them a bit harder to guess. I then made a function called get_word, within this function I asked the user what level they would like to play at. If they chose easy it would generate a word from the easier list if they chose hard it would generate a word from the harder list.