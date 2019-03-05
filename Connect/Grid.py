'''
Created on Mar 4, 2019

@author: jginvincible
'''        

from Player import Player
   
class Grid:
    def __init__(self, rows, columns, player1, player2):
        self.rows = rows
        self.colums = columns
        self.player1 = player1
        self.player2 = player2
        self.matrix = setGrid(rows, columns)
    
    def run(self):
        active = True
        while(active):
            whosTurn(self.player1, self.player2)
            
            

def whosTurn(player_one, player_two):
    if player_one == True:
        slot = input("Which Column Player 1?")
    else:
        slot = input("Which Column Player 2?")
def setGrid(rows, columns):
    Matrix = [["-" for x in range(columns)] for y in range(rows)] 
    return Matrix
    
def printGame(game):
    for row in game.matrix:
        print(row)

print("CONNECT 4")

