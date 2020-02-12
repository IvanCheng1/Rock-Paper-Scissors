#!/usr/bin/env python3

import random
import time

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    name = "Rock Player" # this player only plays rock

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

class RandomPlayer(Player):
    name = "Random Player" # plays randomly every time

    def move(self):
        return random.choice(moves) # random move

class HumanPlayer(Player):
    name = "Human Player" # requires external input

    def move(self):
        human_move = input("Please choose rock, paper or scissors:\n").lower()
        while human_move not in moves: # typo?
            human_move = input("Sorry, please try again.\nPlease choose rock, "
                               "paper or scissors:\n")
        return human_move

class ReflectPlayer(Player):
    name = "Reflect Player" # returns previous opponent's last move

    def move(self):
        try:
            return self.their_move # return opponent last move
        except AttributeError:
            return random.choice(moves) # first round will be random

class CyclePlayer(Player):
    name = "Cycle Player" # cycle through rock, paper and scissors

    def move(self):
        try:
            if self.my_move == 'rock':
                return 'paper' # cycle through rock, paper and scissors
            elif self.my_move == 'paper':
                return 'scissors'
            elif self.my_move == 'scissors':
                return 'rock'
        except AttributeError:
            return random.choice(moves) # first round will be random


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1 # define which class the player is,
        self.p2 = p2 # (cont.) out of random, reflect or human
        self.score_p1 = 0 # game scores set to zero
        self.score_p2 = 0
        self.my_move = '' # reset the previous moves
        self.their_move = ''

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2) == True:
            print("--- Player 1 wins! ---\n")
            self.score_p1 += 1 # score update
        elif beats(move2, move1) == True:
            print("--- Player 2 wins! ---\n")
            self.score_p2 += 1 # score update
        else:
            print("--- It's a draw! ---\n") # no changes to the scores


        self.p1.learn(move1, move2) # learn each others' last moves
        self.p2.learn(move2, move1) # (cont.) and their own

    def play_game(self):
        while True:
            try:
                num_rounds = int(input("How many rounds would you like to "
                                       "play?\n"))
                if num_rounds > 0 and num_rounds <= 100:
                    break
                elif num_rounds <= 0:
                    print("Please enter a positive number")
                elif num_rounds > 100:
                    print("Please enter a smaller number")
            except ValueError:
                print("Please enter an integer")

        print("Game start!") # start game with input number of rounds
        for round in range(num_rounds):
            print(f"Round {round + 1}:")
            self.play_round()
            time.sleep(0.8)

        print("Game over!")

        if self.score_p1 > self.score_p2:
            print("\n******************\n* Player 1 wins! *"
                  "\n******************\n")
        elif self.score_p2 > self.score_p1:
            print("\n******************\n* Player 2 wins! *"
                  "\n******************\n")
        elif self.score_p1 == self.score_p2:
            print("\n****************\n* It's a Draw! *\n****************\n")
        print(f"Score is {self.score_p1}:{self.score_p2} out "
              f"of {num_rounds} round(s)")
        print(f"Your opponent was a {self.p2.name}") # who you last played
        again = input("Would you like to play again? y/n\n").lower()
        if again == 'y':
            game = Game(HumanPlayer(), CyclePlayer())
            game.play_game()
        elif again == 'n':
            print("\nThanks for playing!\n")
            time.sleep(0.8)

Players = [Player(), ReflectPlayer(), CyclePlayer(), RandomPlayer()]
# All the different types of players

if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice(Players))
    game.play_game()
