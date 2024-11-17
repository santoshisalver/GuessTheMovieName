# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 07:26:11 2024

@author: santo
"""

import random

movies = ['anand', 'drishyam', 'nayakan', 'anbe shivam', 'gol maal',
          'vikram vedha', 'black friday', 'dangal']


def create_question(movie):
    n = len(movie)
    letters = list(movie)
    temp = []
    for i in range(n):
        if letters[i] == ' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn = ''.join(str(x) for x in temp)
    return qn


def is_present(letter, movie):
    c = movie.count(letter)
    if c == 0:
        return False
    else:
        return True


def unlock(qn, movie, letter):
    ref = list(movie)
    qn_list = list(qn)
    temp = []
    n = len(movie)
    for i in range(n):
        if ref[i] == ' ' or ref[i] == letter:
            temp.append(ref[i])
        else:
            if qn_list[i] == '*':
                temp.append('*')
            else:
                temp.append(ref[i])
    qn_new = ''.join(str(x) for x in temp)
    return qn_new


def play():
    p1name = input("player1 please enter your name: ")
    p2name = input("player2 please enter your name: ")
    pp1 = 0
    pp2 = 0
    turn = 0
    willing = True
    
    while willing:
        # Player 1's turn
        if turn % 2 == 0:
            print(p1name, 'your turn')
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            modified_qn = qn
            not_said = True
            while not_said:
                letter = input("your letter: ")
                if is_present(letter, picked_movie):
                    modified_qn = unlock(modified_qn, picked_movie, letter)
                    print(modified_qn)
                    d = input('press 1 to guess the movie or 2 to unlock another letter: ')
                    if d == '1':  # Guess the movie
                        ans = input("your answer: ")
                        if ans == picked_movie:
                            pp1 += 1
                            print('Correct!')
                            not_said = False
                            print(p1name, 'your score:', pp1)
                        else:
                            print("Wrong answer. Try again.")
                    elif d == '2':  # Unlock another letter
                        continue  # Continue asking for letters
                else:
                    print(letter, 'not found')

        # Player 2's turn
        else:
            print(p2name, 'your turn')
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            modified_qn = qn
            not_said = True
            while not_said:
                letter = input("your letter: ")
                if is_present(letter, picked_movie):
                    modified_qn = unlock(modified_qn, picked_movie, letter)
                    print(modified_qn)
                    d = input('press 1 to guess the movie or 2 to unlock another letter: ')
                    if d == '1':  # Guess the movie
                        ans = input("your answer: ")
                        if ans == picked_movie:
                            pp2 += 1
                            print('Correct!')
                            not_said = False
                            print(p2name, 'your score:', pp2)
                        else:
                            print("Wrong answer. Try again.")
                    elif d == '2':  # Unlock another letter
                        continue  # Continue asking for letters
                else:
                    print(letter, 'not found')

        # Ask if players want to continue or quit after each round (after both players have taken a turn)
        c = input("Press 1 to continue or 0 to quit: ")
        if c == '0':
            print(p1name, 'your score:', pp1)
            print(p2name, 'your score:', pp2)
            print('Thanks for playing')
            print('Have a nice day')
            willing = False  # Stop the game
        else:
            turn += 1  # Increment the turn counter to switch between players


# Start the game
play()
