'''
Created on Mar 12, 2019

@author: justine
'''
from tkinter import *

from PIL import Image, ImageTk
import tkinter
from random import randint
from Connect.Token_GIF import *
from Connect.Player import *
from Connect.Grid import *
from PIL.FontFile import WIDTH
from distutils import command
from Lib.tkinter.font import BOLD
from pip._vendor.distlib.compat import raw_input

class Token:
    def __init__(self, canvas, x1, y1, x2, y2, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.token = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill=color)  

    def move_ball(self, count, row):
#    token placed on the 1st row
        if row == 0:
            if count < 1:
                deltax = 0
                deltay = 13 # pixels per 20 mx
                self.canvas.move(self.token, deltax, deltay)
                count+=1
                self.canvas.after(20, lambda: self.move_ball(count, row)) # animate ball every 20ms, pass row for token to go to
#    token placed on the 2nd row            
        elif row == 1:
            if count < 6:
                deltax = 0
                deltay = 16 # pixels per 20 ms
                self.canvas.move(self.token, deltax, deltay)
                count+=1
                self.canvas.after(20, lambda: self.move_ball(count, row)) # animate ball every 20ms, pass row for token to go to
#    token placed on the 3rd row
        elif row == 2:
            if count < 16:
                deltax = 0
                deltay = 11.95 # pixels per 20 ms
                self.canvas.move(self.token, deltax, deltay)
                count+=1
                self.canvas.after(20, lambda: self.move_ball(count, row)) # animate ball every 20ms, pass row for token to go to
#    token placed on 4th, 5th, 6th row
        else:
            if count < row * 6:
                deltax = 0
                deltay = 15.20 # pixels per 20 mx
                self.canvas.move(self.token, deltax, deltay)
                count+=1
                self.canvas.after(20, lambda: self.move_ball(count, row)) # animate ball every 20ms, pass row for token to go to
        
class GUI_Game_Board:
    def __init__(self):
    
        self.window = Tk()
        self.window.geometry('1100x750')
        self.window.title("Connect 4 Game")
        self.window.config(bg="white")
       
        self.canvas = Canvas(self.window, width=1100, height=700, bg=self.window['bg'])
        self.canvas.pack(expand=YES, fill=BOTH)

#    make board
        image_path = "C:/Users/justi.JUSTINE-SURFACE/python_practice/Connect_4/Connect/board.png"
        load = Image.open(image_path)
        load = load.resize((1100, 750), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(load)
        self.canvas.create_image(550, 450, image=image) # coordinates for game board image
        
        self.create_triangles()
       
        self.start_game()
        self.window.mainloop()
             


#       creating triangle/buttons for column selection  
    def create_triangles(self):
        triangle_gif = "C:/Users/justi.JUSTINE-SURFACE/python_practice/Connect_4/Connect/ezgif.com-resize.gif"
        origin_x = 215
        origin_y = 120
        triangle1 = ImageButton(self.canvas,bg="white", border="0", command= lambda : self.drop_token(0, self.player1, self.player2))
        triangle1.place(x=origin_x, y=origin_y)
        triangle1.load(triangle_gif)
        origin_x+=100
    
        triangle2 = ImageButton(self.canvas,bg="white", border="0", command= lambda : self.drop_token(1, self.player1, self.player2))
        triangle2.place(x=origin_x, y=origin_y)
        triangle2.load(triangle_gif)
        origin_x+=100
    
        triangle3 = ImageButton(self.canvas,bg="white", border="0", command= lambda : self.drop_token(2, self.player1, self.player2))
        triangle3.place(x=origin_x, y=origin_y)
        triangle3.load(triangle_gif)
        origin_x+=100
    
        triangle4 = ImageButton(self.canvas,bg="white", border="0", command= lambda : self.drop_token(3, self.player1, self.player2))
        triangle4.place(x=origin_x, y=origin_y)
        triangle4.load(triangle_gif)
        origin_x+=100
    
        triangle5 = ImageButton(self.canvas,bg="white", border="0", command= lambda : self.drop_token(4, self.player1, self.player2))
        triangle5.place(x=origin_x, y=origin_y)
        triangle5.load(triangle_gif)
        origin_x+=100
    
        triangle6 = ImageButton(self.canvas,bg="white", border="0", command= lambda : self.drop_token(5, self.player1, self.player2))
        triangle6.place(x=origin_x, y=origin_y)
        triangle6.load(triangle_gif)
        origin_x+=100
    
        triangle7 = ImageButton(self.canvas,bg="white", border="0", command= lambda : self.drop_token(6, self.player1, self.player2))
        triangle7.place(x=origin_x, y=origin_y)
        triangle7.load(triangle_gif)
        origin_x+=100
#   drops tokens according to column selected     
    def drop_token(self, column_number, player1, player2):
        # drops token if it is that players turn
        # take in an extra parameter from the addMove method in Grid class
        # uses the row to calculate where token is dropped in the board
        if self.player1.state == True:
            active, winner, row = self.game.addMove(column_number, player1)
            print(self.player1.name + " dropped a token down column " + str(column_number))
            token = Token(self.canvas, 211 + (100 * column_number) - (0.75 * column_number), 178, 293 + (100 * column_number) - (0.10 * column_number), 258, self.player1.color)
            token.move_ball(0, row)

        else:
            active, winner, row = self.game.addMove(column_number, player2)
            print(self.player2.name + " dropped a token down column " + str(column_number))
            token = Token(self.canvas, 211 + (100 * column_number) - (0.75 * column_number), 178, 293 + (100 * column_number) - (0.10 * column_number), 258, self.player2.color)
            token.move_ball(0, row)

#   moves the token 
# changing player states according to current player turn
        if self.player1.state == True:
            self.player2.state = True
            self.player1.state = False
        else:
            self.player1.state = True 
            self.player2.state = False
            
        self.top.destroy()
        self.update_top_banner()

    # starts the game
    def start_game(self):
        name = raw_input("Player 1, plz enter your Name: ")
        color_one = raw_input("Player 1, choose your color: ")
        
        self.player1 = Player(name, color_one, 0, True)
        
        name2= raw_input("Player 2, plz enter your Name: ")
        color_two = raw_input("Player 2, choose your color: ")
        
        self.player2 = Player(name2, color_two, 0, False)
        
        Matrix = [[0 for x in range(6)] for y in range(7)]
        self.game = Grid(self.player1, self.player2, Matrix)
        self.update_top_banner()
        
    # changing top banner according to player turn
    def update_top_banner(self):
        self.top = tkinter.Frame(master=self.window, width = "150", height = "50", bg = self.window['bg'])
        self.top.place(x=370, y=10)
        if self.player1.state == True:
            label_text = self.player1.name + "'s turn!"
        else:
            label_text = self.player2.name + "'s turn!"

        player_turn_label = tkinter.Label(master = self.top, font = ("Helvetica", 25, BOLD), height=2, width=18, text = label_text, bg=self.window['bg'])
        player_turn_label.pack()
                

        
        
        
game_board = GUI_Game_Board()

