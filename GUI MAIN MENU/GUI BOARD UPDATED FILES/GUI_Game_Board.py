'''
Created on Mar 12, 2019

@author: justine
'''
from tkinter import *

from PIL import Image, ImageTk
import tkinter
from random import randint
from Connect.Token_GIF import *
from Connect.Terminal import *
from Connect.Player import *
from Connect.Grid import *
from PIL.FontFile import WIDTH
from distutils import command

class Token:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.token = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="red")  

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
        image_path = "C:/Users/justi.JUSTINE-SURFACE/python_practice/Connect_4/Connect/board.png"
        triangle_gif = "C:/Users/justi.JUSTINE-SURFACE/python_practice/Connect_4/Connect/ezgif.com-resize.gif"
        load = Image.open(image_path)
        load = load.resize((1100, 750), Image.ANTIALIAS)
        self.canvas = Canvas(self.window, width=1100, height=700, bg=self.window['bg'])
        self.canvas.pack(expand=YES, fill=BOTH)



        image = ImageTk.PhotoImage(load)
        self.canvas.create_image(550, 450, image=image) # coordinates for game board image

#       creating triangle/buttons for column selection  
        origin_x = 215
        origin_y = 120
        triangle = ImageButton(self.canvas,bg="white", border="0", command= lambda : self.drop_token(0))
        triangle.place(x=origin_x, y=origin_y)
        triangle.load(triangle_gif)
        origin_x+=100
    
        triangle = ImageButton(self.canvas,bg="white", border="0", command= lambda : self.drop_token(1))
        triangle.place(x=origin_x, y=origin_y)
        triangle.load(triangle_gif)
        origin_x+=100
    
        triangle = ImageButton(self.canvas,bg="white", border="0", command= lambda : self.drop_token(2))
        triangle.place(x=origin_x, y=origin_y)
        triangle.load(triangle_gif)
        origin_x+=100
    
        triangle = ImageButton(self.canvas,bg="white", border="0", command= lambda : self.drop_token(3))
        triangle.place(x=origin_x, y=origin_y)
        triangle.load(triangle_gif)
        origin_x+=100
    
        triangle = ImageButton(self.canvas,bg="white", border="0", command= lambda : self.drop_token(4))
        triangle.place(x=origin_x, y=origin_y)
        triangle.load(triangle_gif)
        origin_x+=100
    
        triangle = ImageButton(self.canvas,bg="white", border="0", command= lambda : self.drop_token(5))
        triangle.place(x=origin_x, y=origin_y)
        triangle.load(triangle_gif)
        origin_x+=100
    
        triangle = ImageButton(self.canvas,bg="white", border="0", command= lambda : self.drop_token(6))
        triangle.place(x=origin_x, y=origin_y)
        triangle.load(triangle_gif)
        origin_x+=100
        
        self.window.mainloop()
             
#   drops tokens according to column selected     
    def drop_token(self, column_number):
        print(column_number)
        token1 = Token(self.canvas, 211 + (100 * column_number) - (0.75 * column_number), 178, 293 + (100 * column_number) - (0.10 * column_number), 258)
#   moves the token 
        token1.move_ball(0, 5)
        
        
        
game_board = GUI_Game_Board()

