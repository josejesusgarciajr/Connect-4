'''
Created on Mar 4, 2019

@author: justine
'''
import tkinter
from PIL import Image, ImageTk
from Lib.tkinter.font import BOLD

window = tkinter.Tk()
window.title("Connect 4")

window.geometry("1100x750") #You want the size of the app to be 500x500
window.resizable(0, 0) #Don't allow resizing in the x or y direction
window.config(bg = "#67c4ef")


image_path = "C:/Users/justi.JUSTINE-SURFACE/python_practice/Connect_4/Connect/connect4_image.png"


load = Image.open(image_path)
render = ImageTk.PhotoImage(load)
img = tkinter.Label(window, image = render, bg = window['bg'])
img.place(x=-50,y=-150)

bottom = tkinter.Frame(master=window, width = "700", height = "350", bg = window['bg'])
bottom.pack(side="bottom")
bottom.place(y= 450, x = 400)
start_game_button = tkinter.Button(master=bottom, text="START GAME", font = ("Helvetica", 20, BOLD), height=2, width=18, bg="red", fg="white")
start_game_button.pack()

scoreboard_button = tkinter.Button(master=bottom, text="SCOREBOARD", font = ("Helvetica", 20, BOLD), height=2, width=18, bg="red", fg="white")
scoreboard_button.pack(pady = 20)
window.mainloop()
