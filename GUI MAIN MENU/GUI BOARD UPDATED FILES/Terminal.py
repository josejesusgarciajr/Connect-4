'''
Created on Mar 4, 2019

@author: jginvincible
'''
# MODULE NOT NEEDED -> GAME RUNS IN GUI
from Connect.Player import Player
from Connect.Grid import Grid
from pip._vendor.distlib.compat import raw_input

class Terminal:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        
name = raw_input("Player 1, plz enter your Name: ")
color_one = raw_input("Player 1, choose your color: ")

player1 = Player(name, color_one, 0, True)

name2= raw_input("Player 2, plz enter your Name: ")
color_two = raw_input("Player 2, choose your color: ")

player2 = Player(name2, color_two, 0, False)

Matrix = [[0 for x in range(6)] for y in range(7)]
game = Grid(player1, player2, Matrix)

def printGame(game):
    for row in game:
        print(row)

def runGame(game): # This is where the game is run from
    active = True
    while(active):
        (col, player, nextTurn) = game.whosTurn(player1, player2)
        active, winner = game.addMove(col, player)
        if active == False:
            print(winner.name + " WON!")
        game.printGame()
        if game.checkForDraw():
            print("DRAW!")
            break
        player.state = False
        nextTurn.state = True
        
runGame(game)
