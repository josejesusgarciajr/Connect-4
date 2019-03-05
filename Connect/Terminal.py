'''
Created on Mar 4, 2019

@author: jginvincible
'''

from Player import Player
from Grid import Grid

class Terminal:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        
player1 = raw_input("Player 1, plz enter your Name: ")
color_one = raw_input("Player 1, choose your color: ")

player_one = Player(player1, color_one, 0, True)

player2= raw_input("Player 2, plz enter your Name: ")
color_two = raw_input("Player 2, choose your color: ")

player_two = Player(player2, color_two, 0, False)

game = Grid(6, 7, player1, player2)

game.run()