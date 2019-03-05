'''
Created on Mar 4, 2019

@author: jginvincible
'''        

from Player import Player
from inspect import stack
from __builtin__ import True
   
class Grid:
    def __init__(self, player1, player2, matrix):
        self.player1 = player1
        self.player2 = player2
        self.matrix = matrix
        
    def addMove(self, column, player):
        row = len(self.matrix[column]) - 1

        (notFull, row) = self.columnNotFull(column)
        
        if notFull:
            self.matrix[column][row] = player.color # if Not FUll (ADD TO COLUMN)
        else:
            notValidEntry = True
            while notValidEntry:
                column = input(player.name + " choose a column that is not full: ") - 1
                validEntry, row = self.columnNotFull(column)

                if validEntry:
                    self.matrix[column][row] = player.color
                    notValidEntry = False
        printGame(self.matrix)
    
    def whosTurn(self, player1, player2):
        if player1.state == True:
            col = input("Which Column Player 1?")
            return (col -1), player1, player2
        else:
            col = input("Which Column Player 2?")
            return (col - 1), player2, player1
        
    def columnNotFull(self, column):
        row = len(self.matrix[column]) - 1
        while (self.matrix[column][row] != 1 or self.matrix[column][row]) != 2 and row >= 0:
            if self.matrix[column][row] == 0:
                return (True, row)
            row -= 1
        return (False , -1)
 
def printGame(game):
    for row in game:
        print(row)


