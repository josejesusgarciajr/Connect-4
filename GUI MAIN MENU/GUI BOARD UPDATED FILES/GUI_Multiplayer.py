from tkinter import *
from tkinter.font import BOLD

from PIL import Image, ImageTk
import tkinter
from Tools.scripts import highlight

class GUI_Multiplayer:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1100x750')
        self.window.title("Connect 4 User Input")
        self.window.config(bg="#1dace7")

        # Set background image

        image_path = "C:/Users/justi.JUSTINE-SURFACE/python_practice/Connect_4/Connect/Connect-4-Header.png"

        load = Image.open(image_path)
        load = load.resize((1100, 750), Image.ANTIALIAS)

        canvas = Canvas(self.window, width=1100, height=700, bg=self.window['bg'])
        canvas.pack(expand=YES, fill=BOTH)

        # Add a backgrund image to canvas at point (0,0)

        image = ImageTk.PhotoImage(load)
        canvas.create_image(550, 400, image=image)
        # Frame to center player entries and color choices

        frame = Frame(self.window, width=750, height=500, bg=self.window['bg']).place(x=175,y=100)

        # Create labels for player 1 and player 2 input

        self.player1_label = Label(frame, font=("Impact", 24, BOLD), height=2, width=18, text="Player 1",
                                   bg='#fff263').place(x=200, y=100)
        self.player2_label = Label(frame, font=("Impact", 24, BOLD), height=2, width=18, text="Player 2",
                                   bg='#f45642').place(x=600, y=100)

        self.player1_name = StringVar(self.window) #to retrive data in another method using self
        self.player2_name = StringVar(self.window)

        # Player 1 entry box data with name placeholder

        self.player1_entry = Entry(frame, bd=5, textvariable=self.player1_name)
        self.player1_entry.insert(0, "Enter Player 1 Name ")
        self.player1_entry.place(width=250, height=50, x=225,y=200)
        self.player1_entry.bind("<Button-1>", self.clear_entry1)

        # Player 2 entry box data with name placeholder

        self.player2_entry = Entry(frame, bd=5, textvariable=self.player2_name)
        self.player2_entry.insert(0, "Enter Player 2 Name ")
        self.player2_entry.place(width=250, height=50, x=625,y=200)
        self.player2_entry.bind("<Button-1>", self.clear_entry2)

        Label(frame, text="Choose a color", font=("Helvetica", 18, BOLD), height=2, width=14, bg=self.window['bg'],
              fg="white").place(x=250, y=275)

        # Radio buttons to depict color choices for tokens

        self.player1_colorvar = IntVar(self.window) #to retrive data in another method using self
        self.player2_colorvar = IntVar(self.window)

        CHOICES = [('Blue', 1), ('Green', 2), ('Red', 3), ('Yellow', 4)]
        self.player1_colorvar.set(1)  # set the default option

        shift_y = 350
        for choice, val in CHOICES:
            radio_button = Radiobutton(frame, text=choice, font=("Helvetica", 16, BOLD), indicatoron=0, padx=20,
                                       width=10, variable=self.player1_colorvar, value=val, bg=choice,
                                       fg="white").place(x=250, y=shift_y)
            shift_y += 50


        Label(frame, text="Choose a color", font=("Helvetica", 18, BOLD), height=2, width=14, bg=self.window['bg'],
              fg="white").place(x=650, y=275)

        # Player 2 radio buttons for color choices

        self.player2_colorvar.set(2)  # set the default option

        shift_y = 350
        for choice, val in CHOICES:
            radio_button = Radiobutton(frame, text=choice, font=("Helvetica", 16, BOLD), indicatoron=0, padx=20,
                                       width=10, variable=self.player2_colorvar, value=val, bg=choice,
                                       fg="white").place(x=650, y=shift_y)
            shift_y += 50



        # Button to initiate the game

        button = Button(canvas, text="PLAY", font=("Impact", 25, BOLD), height=1, width=18, bg="blue",
                        fg="white", command=self.play)
        button.place(x=415, y=625)

        self.window.mainloop()

    def play(self):
        color_options = ["Blue", "Green", "Red", "Yellow"]
        print("*****PLAY CONNECT 4*******")
        print("Player 1 info ", self.player1_name.get(), color_options[self.player1_colorvar.get() - 1])
        print("Player 2 info ", self.player2_name.get(), color_options[self.player2_colorvar.get() - 1])

        # Hides the placeholder text in entry box on mouse click

    def clear_entry1(self, event):
        self.player1_entry.delete(0, END)

    def clear_entry2(self, event):
        self.player2_entry.delete(0, END)

# GUI_Multiplayer()