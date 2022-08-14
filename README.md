[PythonPP3pdf.pdf](https://github.com/thesherifff/Battleships-INC/files/9332998/PythonPP3pdf.pdf)


# Battleships

## Introduction

This project is a battleships game that uses the Python code language, which is deployed via Heroku.
The goal is to beat the CPU by finding and destroying all its battleships before it destroys your ship. Each battleship is in a 1x1 area on the board, and you must find all of them on the board.

https://battleshipinc.herokuapp.com/


## Strategy

## Project Goals

My ambition was to create an entertaining game that affords interactive features to the user and to display my use basic use of the Python language. The idea is that the user will play vs the computer, thus making the game more challenging. 

### User Goals:

I believe that good design allows users to understand and engage with the product with minimal effort.

-As a new player, I want to be confronted with the rules of the game.
-As a new player, I want to effortlessly understand the rules of the game.
-As a new player, I want to be challenged and given a clear objective, i.e. Win the game.

Returning Visitor Goals
-As an experienced player, I want to win against the CPU.

Frequent User Goals
-As a Frequent User, I want to stay updated and hone my skills.

### User Expectations:
-A fun and engaging game that allows for a winner and loser.
-Clear and easy rules to follow
-The game is fun to replay.

## Rules on how to play

Battleships is a game that requires two players to play. In my iteration, you will be playing vs the CPU. The user will enter a value between 0-9 in which you state in order to guess the location of all three ships on the board. Both players receive eight guesses, and if the user has used all of their guesses on the first ship, the game will sadly end. The player will see where their ships are marked, highlighted by an S. If the players miss on their guesses, the board will be marked with an O, and the hits are highlighted by an X. Once the user has played their guess, the CPU will automatically reply with its own guess. The user and computer will alternate, both taking turns to guess. The game is finished when the user or computer has guessed the location of the opponent's ships correctly or when either player has guessed incorrectly eight times.

## Features

### Current Features

-Random ship generation
-The user and computer ships are spawned at random in the play area.
-The user's ship location will be printed on the user's board; this is marked with an "S."
-Multiple battleships - each opponent has three ships to sink.

-Play against the computer, and the computer will automatically return with a guess.
-Allows for user input

-Input validation
  -Ensured only integers and numbers were allowed as inputs.
  -Message to show when a value that falls outside of the game's range.
  -Error message when the same guess is filed repeatedly.

### Future Features
-Allow player to set board size.
-Allow players to play against each other.
-Increase difficulty
-Decrease amount of guesses
-Timer function
-Change cosmetic options

##Testing

[PEP8pythonvalidator.pdf](https://github.com/thesherifff/Battleships-INC/files/9333001/PEP8pythonvalidator.pdf)



The project has been manually tested using the following methods:

-Entered incorrect inputs to ensure warning messages were being returned correctly. 
-As the project was being coded, New lines of code were tested through the terminal each time to make sure the *functions functioned correctly.
-Used Heroku to test the game.
-Validated using the following testing method
PEP8 I tested the code through PEP8's validator. As you can see below, there are no errors.


## Deployment
I used Heroku to deploy my final project to the cloud. To do this, I had to:

1.  Pushed the code to Github
2.  Created an account on Heroku 
3.  Logged into Heroku
4.  Created a new app.
5.  Chose a name for the app name and select Europe as the region.
6.  Connected to GitHub.
7.  I searched for my repo.
8.  Selected the relevant repo to deploy.
9.  Select the settings tab.
10. Included buildpack
11.  Select Python, then save changes.
12. Select Nodejs, then save changes.
13. Confirmed  Heroku/Python is included, followed by Heroku/Nodejs.
14. Navigate to the deploy tab
15. Scroll down to Manual Deploy and press Deploy Branch.


##Credits

*GitHub Python Template Code Institute
*Heroku deployment instructions from Code Institute
*Code was built in large thanks iKelvvv, who I had used as a template to help build my Battleship game also. 
