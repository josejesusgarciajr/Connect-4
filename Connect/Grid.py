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
        
    def addMove(self, column, player): # Add's a move if valid
        row = 1
        if self.inRange(column):            # First check if the column is in range ( 1 - 7)
            row = len(self.matrix[column]) - 1  # If it is, then get the number of rows to check
        else:
            notInRange = True           # If not in range, 
            while notInRange:                   # Loop Until Player
                column = input("RANGE MUST BE BETWEEN 1 - 7: ") - 1
                if self.inRange(column):            # Enters a Valid Range
                    row = len(self.matrix[column]) - 1
                    notInRange = False
        
        notFull = False
        if self.inRange(column):
            notFull, row, column = self.columnNotFull(column) # checks if a column is full or not
        else:
            notInRange = True
            while notInRange:
                column = input(player.name + " input range 1-7: ") - 1
                if self.inRange(column):
                    notFull, row, column = self.columnNotFull(column) # checks if a column is full or not
                    notInRange = False

        if notFull:
            self.matrix[column][row] = player.color # if Not FUll (ADD TO COLUMN)
        else:
            notValidEntry = True                # if column is full
            while notValidEntry:
                column = input(player.name + " choose a column that is not full: ") - 1
                validEntry, row, column = self.columnNotFull(column)  # continue to ask until user
                                     
                if validEntry:                  #enters a valid column (COLUMN THAT IS NOT FULL)
                    self.matrix[column][row] = player.color
                    notValidEntry = False
        printGame(self.matrix)
    
    def whosTurn(self, player1, player2):   # checks whos turn it is
        if player1.state == True:           
            col = input("Which Column Player 1?")
            return (col -1), player1, player2
        else:
            col = input("Which Column Player 2?")
            return (col - 1), player2, player1
        
    def columnNotFull(self, column):        # Checks if a given column is full
        if self.inRange(column):            # Checks if column is in range
            row = len(self.matrix[column]) - 1
            while (self.matrix[column][row] != 1 or self.matrix[column][row]) != 2 and row >= 0:
                if self.matrix[column][row] == 0:
                    return (True, row, column)      # Loop to find a row to put the players move
                row -= 1
        else:                           # If not in range
            notInRange = True       
            while notInRange:                   # Loop  to find a valid column
                column = input("Input range 1-7: ") - 1     
       
                if self.inRange(column):                # that is in range
        
                    row = len(self.matrix[column]) - 1
                    while (self.matrix[column][row] != 1 or self.matrix[column][row]) != 2 and row >= 0:
                        print(self.matrix[column][row])
                        if self.matrix[column][row] == 0:
                            return (True, row, column)          # and that is not full
                        row -= 1
                    notInRange = False
            
        return (False , -1, column)
    
    def inRange(self, column):
        if column <= 6 and column >= 0:     # simply checks if the column is in range
            return True                 # (1 - 7)
        return False
 
def printGame(game):
    for row in game:
        print(row)


