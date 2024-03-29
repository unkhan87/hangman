# Hangman

Hangman is a guessing game and is usually played by two or more people, where one player thinks of a word while the other players guess what the word is by guessing one letter at a time until the whole word is revealed or they run out of tries.
The game is usually played with a Paper-and-pencil however I decided to create electronic version of the game that you can play against the computer rather than playing against another person.
I've used python programming language to program this game. Number of different functions have been created in order to achieve different tasks for this game.

[Click here to go to the live website!](https://uk-hangman.herokuapp.com/)

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
        - When the game ends the user is presented with an option if they like play again or if they would like to quit. Again option 1 for 'Yes' and option 2 for 'No'.

- Does it make it clear to the user how many tries they have left.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - When the user gets a guess wrong it will print out a section of the hangman image that shows how many tries the user has left in the game.

## Changes throughout the process

The initial thought process was to create a list of words within one file and use the while loop to get the words from the list however this was aboloshed after the code was looking over-populated and after watching several youtube videos and going through alot of blogs I found out a way to create new file and import the words from the words file to the main run.py file.

Initial idea was to give display 6 lives on the user screen and then to decrement it if the user get the letter wrong. However, then this would have never been a traditional hangman and then I decided to implement a hangman image in my code.

ASCII art was never in my initial plan however then I learned how easy it was to implement ASCII art in the python code.

## Features

### Welcome Page
- This is the first page user see when the app loads. The welcome page includes ASCII art and asks user for their name and then it greets the user followed by the users name. And then it give users the option to either see instructions or to play the game.

<img src="images/hangman_welcome.png" alt="Welcome">

<img src="images/hangman_welcome_greet.png" alt="Greetings">

### Instructions
- This section give users the instructions regarding how to play the game. And introduce the user with a guidance on how to play the game.

<img src="images/instructions_hangman.png" alt="Instructions">

### Game
- When the user starts the game, it shows the user the length of the word and display gallows. It request the user to guess the their first letter.

<img src="images/start_hangman.png" alt="Start Game">

- While the user is playing the game the program also displays the letters the users have used and if the user insert any used letter it gives them a message that the letter has already been used.

<img src="images/hangman_duplicate_guess.png" alt="Already Used Letter">

- The program also displays that if the user has guessed the letter correctly shows a message to the user that the guessed word is correct and accordingly if the user has guessed it wrong the program will accordingly show them the message followed by the wrongly guessed letter.

<img src="images/hangman_correct_guess.png" alt="Correct Guess">

<img src="images/hangman_wrong_guess.png" alt="Incorrect Guess">

### Loosing Message
- If the user loose the game they will get an option if they want to play again or not. Option 1 for 'Yes' and Option 2 for 'No'.

<img src="images/hangman_out_of_tries.png" alt="Out of tries">

### End Message
- If the user chooses not to play again they will get a goodbye message.

<img src="images/hangman_end_message.png" alt="Goodbye Message">

### Winning Message
- Currently there's a bug in displaying this message. If the user guess the word correctly it does not give end the game and asks user to keep guessing. I tried to implement different solutions however I end up creating errors on the while loop.

### Future Features
- For future development I would like to give the user more options like different levels of difficulty and introduce the option of different languages as well.

- Find a way to resolve the bug without effecting the while loop.

## Testing

### Python
I used PEP8 validator to test my code.

The python results came with the following:

<img src="images/pep8_list_of_errors.png" alt="Initial PEP8 Results">

- Trailing white space erros were fixed by removing the space from the last character.

- Continuation line under-indented for visual indent was resolved by indenting the first line to the opening parenthses.

- line too long errors was mainly in the input section and the instructions section of the code to fix this issues I edited the long lines and made them into multiple shorter lines.

- Whitespace errors were removed by deleting the whitespace from my code.

- Please see the results below after the errors were fixed.

<img src="images/pep8_result.png" alt="Results after the issues were resolved">

### Manual Testing
- Testing started from the welcome message. The input and greeting was tested to check if its functioning properly and if the user is getting the result as expected.

- Where the program asks for an input from the user like Option 1 for 'Yes' or Option 2 for 'No' I tested what would happen if the user inserted an invalid key and hence with the help of while loop I've managed to add a condition where the user input any invalid character the program throws the user an error message saying invalid input and request to either input 1 or 2.

<img src="images/welcome_invalid_input.png" alt="Invalid input for the welcome page">

- Next I tested if the game starts if the user does not want to view the instructions. And it does.

- I also tested if the user wants to see the instructions and if the results were as expected. 

- On to the actual game I tested if the program is only taking alphabets and is not accepting any invalid characters.

- If used letter option is getting displayed to the user.

- Already gussed letter functionality is working and it is.

- The messages for the correct and incorrect guess is showing followed by the guessed letter.

-  And if the game ending messages are shwoing correctly and when the game ends if the user is prompted with a play again option.

- Tested if the hangman image is working as its suppose to like displaying a section of the hangman image if the user gets the letter wrong and if the user gets it right nothing happens to the image.

## Bugs

### Remaining Bugs
- When the user guess the word correctly with lives remaining the game doesn't end and ask user to keep guessing until the hangman image fully gets completed in other words when the user is out of tries.

## Deployment

1. I went over to my Heroku dashboard and clicked on 'create a new app'.
2. I chose a name for my app; every app must have a unique name so I couldn't call it hangman as this was already taken so I went for uk_hangman.
3. Selected my region and clicked create app. 
4. I then went to the tab at the top of the page and clicked on settings. 
6. I added two (python & node.js) making sure they are in the correct order.
7. I scrolled back up to the tab at the top and clicked deploy.
8. I selected github as the deployment method and clicked connect to github.
9. Once this is selected, I then searched for my github repository name, and connected to the correct repository.
10. Then I scrolled down, and choose to manually deploy my repository from Github.
10. Once the build was completed I clicked on the view button to check if the app is running as expected and played the game to test if its working.

## Credits

- [PEP8 Validator](http://pep8online.com/) - was used to check the code was valid.

- Youtube tutorials - [Hangman Tutorial by Kylie Ying] (https://www.youtube.com/watch?v=cJJTnI22IF8)
                      [Tutorial by Kite] (https://www.youtube.com/watch?v=m4nEnsavl6w&t=406s)

- Hangman Image - https://inventwithpython.com/invent4thed/chapter8.html

- [Google developer docs for python](https://developers.google.com/edu/python) - helped me with the while and for loops and functions. 

- Marcel - My mentor helped was very helpful throughout the process helping me with the code and giving me ideas how to structure my game.

