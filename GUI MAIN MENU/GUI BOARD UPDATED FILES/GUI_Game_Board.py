'''
Created on Mar 12, 2019

@author: justine
'''
from tkinter import *

from PIL import Image, ImageTk
import tkinter
from random import randint
from Connect.Token_GIF import *
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

    def move_ball(self):
        deltax = 0
        deltay = 8
        self.canvas.move(self.token, deltax, deltay)
        self.canvas.after(200, self.move_ball)
        
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

        # Add a backgrund image to canvas at point (0,0)
#         self.tri = Image.open(triangle_gif)
#         self.tri = self.tri.resize((65, 45), Image.ANTIALIAS)
#         self.tri_image = ImageTk.PhotoImage(self.tri);
       
        

        image = ImageTk.PhotoImage(load)
        self.canvas.create_image(550, 450, image=image) # coordinates for image
        # CREATING CIRCLES
#         canvas.create_oval(10, 10, 80, 80, outline = "red", fill="red", width=2)
        origin_x = 215
        origin_y = 120
#         t1 = self.canvas.create_polygon((origin_x + 0, origin_y + 0, origin_x + 70, origin_y + 0, origin_x + 35, origin_y + 50), fill="red")
#         move_x = 100
#         for x in range(6):
#             self.canvas.create_polygon((origin_x + 0 + move_x, origin_y + 0, origin_x + 70 + move_x, origin_y + 0, origin_x + 35 + move_x, origin_y + 50), fill="red")
#             move_x += 100
        # Frame to center player entries and color choices
        triangle = ImageButton(self.canvas,bg="white", border="0", command= lambda : self.drop_token(0))
        triangle.place(x=origin_x, y=origin_y)
        triangle.load('C:/Users/justi.JUSTINE-SURFACE/python_practice/Connect_4/Connect/ezgif.com-resize.gif')
        origin_x+=100
    
        triangle = ImageButton(self.canvas,bg="white", border="0", command= lambda : self.drop_token(1))
        triangle.place(x=origin_x, y=origin_y)
        triangle.load('C:/Users/justi.JUSTINE-SURFACE/python_practice/Connect_4/Connect/ezgif.com-resize.gif')
        origin_x+=100
    
        triangle = ImageButton(self.canvas,bg="white", border="0", command= lambda : self.drop_token(2))
        triangle.place(x=origin_x, y=origin_y)
        triangle.load('C:/Users/justi.JUSTINE-SURFACE/python_practice/Connect_4/Connect/ezgif.com-resize.gif')
        origin_x+=100
    
        triangle = ImageButton(self.canvas,bg="white", border="0", command= lambda : self.drop_token(3))
        triangle.place(x=origin_x, y=origin_y)
        triangle.load('C:/Users/justi.JUSTINE-SURFACE/python_practice/Connect_4/Connect/ezgif.com-resize.gif')
        origin_x+=100
    
        triangle = ImageButton(self.canvas,bg="white", border="0", command= lambda : self.drop_token(4))
        triangle.place(x=origin_x, y=origin_y)
        triangle.load('C:/Users/justi.JUSTINE-SURFACE/python_practice/Connect_4/Connect/ezgif.com-resize.gif')
        origin_x+=100
    
        triangle = ImageButton(self.canvas,bg="white", border="0", command= lambda : self.drop_token(5))
        triangle.place(x=origin_x, y=origin_y)
        triangle.load('C:/Users/justi.JUSTINE-SURFACE/python_practice/Connect_4/Connect/ezgif.com-resize.gif')
        origin_x+=100
    
        triangle = ImageButton(self.canvas,bg="white", border="0", command= lambda : self.drop_token(6))
        triangle.place(x=origin_x, y=origin_y)
        triangle.load('C:/Users/justi.JUSTINE-SURFACE/python_practice/Connect_4/Connect/ezgif.com-resize.gif')
        origin_x+=100
    
       
        
#         ball2 = Token(self.canvas)
#         
#         ball2.move_ball()

        self.window.mainloop()  
    def drop_token(self, column_number):
        print(column_number)
        token1 = Token(self.canvas, 211 + (100 * column_number), 213, 291 + (100 * column_number), 289)
        token1.move_ball()

                        
GUI_Game_Board()
# initialize root Window and canvas
# root = Tk()
# root.title("Balls")
# root.resizable(False,False)
# canvas = Canvas(root, width = 300, height = 300)
# canvas.pack()
# 
# # create two ball objects and animate them
# ball1 = Token(canvas)
# 
# ball2 = Token(canvas)
# 
# ball1.move_ball()
# ball2.move_ball()
# 
# root.mainloop()

