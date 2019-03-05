'''
Created on Mar 4, 2019

@author: jginvincible
'''

from Player import Player
from Grid import Grid

class Termainal:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        
p_one_name = raw_input("Player 1, plz enter your Name: ")
color_one = raw_input("Player 1, choose your color: ")

player_one = Player(p_one_name, color_one, 0, True)

p_two_name = raw_input("Player 2, plz enter your Name: ")
color_two = raw_input("Player 2, choose your color: ")

player_two = Player(p_two_name, color_two, 0, False)

game = Grid(6, 7)

game.run()