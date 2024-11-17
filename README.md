# Movie Guessing Game

## Overview
This is a simple console-based two-player movie guessing game, where players take turns guessing a randomly chosen movie. 
The objective is to guess the movie title by guessing individual letters, and the game keeps track of the score for each player.

## How to Play

1. **Player 1** and **Player 2** take turns guessing letters in the movie name.
2. Each correct letter guess reveals the letter in the movie name.
3. After each letter guess, players can either:
   - **Guess the full movie name** by pressing `1`.
   - **Unlock another letter** by pressing `2`.
4. Players can continue playing until they choose to quit. After each round (both players take their turns), they will be asked whether they want to continue or quit.
   - Press `1` to continue.
   - Press `0` to quit.

## Features
- **Two-Player Game**: Each player alternates taking turns.
- **Score Tracking**: The score is updated after each correct guess.
- **Random Movie Selection**: Movies are randomly chosen from a predefined list.
- **Guessing Mechanics**: Players can guess individual letters or try to guess the entire movie name.
- **Quit Option**: Players can quit the game at any time by entering `0`.

##Example Game Flow
<br>
player1 please enter your name: santoshi
<br>
player2 please enter your name: saipriya
<br>
santoshi your turn
<br>
******
<br>
your letter: a
<br>
*a**a*
<br>
press 1 to guess the movie or 2 to unlock another letter: 2
<br>
your letter: n
<br>
*an*a*
<br>
press 1 to guess the movie or 2 to unlock another letter: 1
<br>
your answer: dangal
<br>
Correct!
<br>
santoshi your score: 1
<br>
Press 1 to continue or 0 to quit: 1
<br>
saipriya your turn
<br>
********
<br>
your letter: d
<br>
d*******
<br>
press 1 to guess the movie or 2 to unlock another letter: 2
<br>
your letter: m
<br>
d******m
<br>
press 1 to guess the movie or 2 to unlock another letter: 2
<br>
your letter: p
<br>
p not found
<br>
your letter: a
<br>
d*****am
<br>
press 1 to guess the movie or 2 to unlock another letter: 1
<br>
your answer: drishyam
<br>
Correct!
<br>
saipriya your score: 1
<br>
Press 1 to continue or 0 to quit: 0
<br>
santoshi your score: 1
<br>
saipriya your score: 1
<br>
Thanks for playing
<br>
Have a nice day
<br>
