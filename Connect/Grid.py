'''
Created on Mar 4, 2019

@author: jginvincible
'''        

from Player import Player
from inspect import stack
   
class Grid:
    def __init__(self, player1, player2, matrix):
        self.player1 = player1
        self.player2 = player2
        self.matrix = matrix
        
    def addMove(self, column, player):
        row = len(self.matrix[column]) - 1
        print("LENGHT OF COLUMN: " + str(row))
        while(self.matrix[column][row] != 0):
            row -= 1
        self.matrix[column][row] = player.color
        printGame(self.matrix)
    
    def whosTurn(self, player1, player2):
        if player1.state == True:
            col = input("Which Column Player 1?")
            return (col -1), player1, player2
        else:
            col = input("Which Column Player 2?")
            return (col - 1), player2, player1
 
def printGame(game):
    for row in game:
        print(row)


