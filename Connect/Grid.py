'''
Created on Mar 4, 2019

@author: jginvincible
'''        
from Terminal import Terminal
from Player import Player
   
class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.colums = columns
        self.matrix = setGrid(rows, columns)
    
    def run(self):
        active = True
        while(active):
            slot = whosTurn(Terminal.p_one_name, Terminal.player_two)
            
            

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

game = Grid(6,7)
print("CONNECT 4")
printGame(game)
