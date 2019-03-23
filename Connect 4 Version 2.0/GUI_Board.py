from tkinter import *
from tkinter.font import BOLD

from PIL import Image, ImageTk
import tkinter
from connect.Token_GIF import *
from connect.Player import *
from connect.Grid import *


class Token:
    # Creates the chip to be dropped in the board
    def __init__(self, canvas, x1, y1, x2, y2, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.token = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill=color)

    # Based on the rules of the game, the chip is dropped to the last row
        # Per row the chip travels a different distance
    def move_ball(self, token, count, row):
        #    token placed on the 1st row
        if row == 0:
            if count < 1:
                deltax = 0
                deltay = 13  # pixels per 20 mx
                self.canvas.move(self.token, deltax, deltay)
                count += 1
                self.canvas.after(20, lambda: self.move_ball(token, count, row))  # animate ball every 20ms, pass row for token to go to
        #    token placed on the 2nd row
        elif row == 1:
            if count < 6:
                deltax = 0
                deltay = 16  # pixels per 20 ms
                self.canvas.move(self.token, deltax, deltay)
                count += 1
                self.canvas.after(20, lambda: self.move_ball(token, count, row))  # animate ball every 20ms, pass row for token to go to
        #    token placed on the 3rd row
        elif row == 2:
            if count < 16:
                deltax = 0
                deltay = 11.95  # pixels per 20 ms
                self.canvas.move(self.token, deltax, deltay)
                count += 1
                self.canvas.after(20, lambda: self.move_ball(token, count, row))  # animate ball every 20ms, pass row for token to go to
        #    token placed on 4th, 5th, 6th row
        else:
            if count < row * 6:
                deltax = 0
                deltay = 15.20  # pixels per 20 mx
                self.canvas.move(self.token, deltax, deltay)
                count += 1
                self.canvas.after(20, lambda: self.move_ball(token, count, row))  # animate ball every 20ms, pass row for token to go to


class GUI_Board:

    def __init__(self, player1_name, player2_name, player1_color, player2_color):
        print("******GUI Board********")
        self.window = Toplevel()
        self.window.geometry('1100x750')
        self.window.title("Connect 4 Game")
        self.window.config(bg="white")

        # referencing to the data collected in the input menu
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_color = player1_color
        self.player2_color = player2_color

        self.canvas = Canvas(self.window, width=1100, height=700, bg=self.window['bg'])
        self.canvas.pack(expand=YES, fill=BOTH)

        self.make_board()
        self.token_color = player1_color

        # Creates the hovering token with initial color of player 1
        self.circle = self.canvas.create_oval(211 + (100) - (0.75), 95, 293 + (100) - (0.10), 175, fill=self.token_color)

        # Clicking and motion of token is tracked by these functions
        self.canvas.bind('<Button-1>', self.clicked)
        self.canvas.bind('<Motion>', self.callback)
        self.canvas.pack()


        self.start_game()
        self.window.mainloop()

    # Makes the board for the game using an image
    def make_board(self):
        self.image_path = "/Users/Nikita/Documents/workspacepycharm/Connect4/connect/board.png"
        self.load = Image.open(self.image_path)
        self.load = self.load.resize((1100, 750), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.load)
        self.canvas.create_image(550, 450, image=self.image)  # coordinates for game board image

    # When mouse is on the window, a token appears and follows the mouse
    def callback(self, event):
        x, y = event.x, event.y
        self.canvas.coords(self.circle, x - 40, 95, x + 40, 175)

    # When player clicks in the column area to drop the token the x coordinate is extracted
    def clicked(self, event):
        #global column_number
        print("Clicked at:")
        print("x = " + str(event.x), "and y = ", str(event.y))

        # find the column clicked
        self.column_number = self.find_column(event)
        print("column # ", str(self.column_number))

        self.drop_token(self.column_number, self.player1, self.player2)  # the number designates the column of the board

        # removes previously created circle to identify player 2's turn
        self.canvas.delete(self.circle)

        # changes the color of the token to display whose turn it is
        if self.player1_color == self.token_color:
            self.token_color = self.player2_color
        else:
            self.token_color = self.player1_color

        self.circle = self.canvas.create_oval(211 + (100 * self.column_number) - (0.75 * self.column_number), 95, 293 + (100 * self.column_number) - (0.10 * self.column_number), 175, fill=self.token_color)
        self.window.update()

    # Finds the column number based on the x coordinates of where the token was clicked
        # Columns identified from 0 to 6 representing 1 to 7
    def find_column(self, event):
        print("x coordinates: ",str(event.x))
        if (event.x < 280):
            self.column_number = 0
        elif (event.x > 281 and event.x < 380):
            self.column_number = 1
        elif (event.x > 381 and event.x < 480):
            self.column_number = 2
        elif (event.x > 481 and event.x < 580):
            self.column_number = 3
        elif (event.x > 581 and event.x < 680):
            self.column_number = 4
        elif (event.x > 681 and event.x < 780):
            self.column_number = 5
        elif( event.x > 781 and event.x < 880):
            self.column_number = 6

        return self.column_number

    # Drops tokens according to column selected
    def drop_token(self, column_number, player1, player2):
        # drops token if it is that players turn
        # takes in an extra parameter from the addMove method in Grid class (passes in row from Grid class addMove function)
        # uses the row to calculate where token is dropped on the board
        if self.player1.state == True:
            active, winner, row = self.game.addMove(column_number, player1)
            token = Token(self.canvas, 211 + (100 * column_number) - (0.75 * column_number), 178,
                          293 + (100 * column_number) - (0.10 * column_number), 258, self.player1.color)

            self.player2.state = True
            self.player1.state = False
        else:
            active, winner, row = self.game.addMove(column_number, player2)
            token = Token(self.canvas, 211 + (100 * column_number) - (0.75 * column_number), 178,
                          293 + (100 * column_number) - (0.10 * column_number), 258, self.player2.color)
            self.player1.state = True
            self.player2.state = False

        print("current row is ", str(row))

        token.move_ball(token, 0, row)

        if (row == 0):
            print("no more rows left")

        #    game over, winner is found
        #    destroy the top banner and create a new one with winner name
        if active == False:
            print("winner has been found!!!!!!")
            self.top.destroy()
            # whoever wins this round gets to start in the next round
            if self.player1.state:
                self.player2.state = True
                self.player1.state = False
            else:
                self.player1.state = True
                self.player2.state = False

            self.update_top_banner(winner=winner, active=active)

        #    no winner detected, keep playing
        else:
            self.top.destroy()
            self.update_top_banner(None, None)

    # starts the game
    def start_game(self):
        self.player1 = Player(self.player1_name, self.player1_color, 0, True)

        self.player2 = Player(self.player2_name, self.player2_color, 0, False)

        Matrix = [[0 for x in range(6)] for y in range(7)]
        self.game = Grid(self.player1, self.player2, Matrix)
        self.update_top_banner(None, None)
        self.show_scoreboard()

    # new game after win
    def show_new_game(self):
        self.new_game = tkinter.Frame(master=self.window, width="200", height="50", bg=self.window['bg'])
        self.new_game.place(x=970, y=20)
        button = tkinter.Button(master=self.new_game, text="NEW GAME", font=("Helvetica", 12, BOLD), height=2, width=18,
                                bg="#61bffa", fg="white", highlightbackground="blue", command=self.start_new_game)
        button.pack()

    def start_new_game(self):
        self.canvas.delete("all")
        self.make_board()

        print("Player 1 state ", self.player1.state)
        print("Player 2 state", self.player2.state)
        if self.player1.state:
            self.token_color = self.player1_color
        else:
            self.token_color = self.player2_color
            
        self.circle = self.canvas.create_oval(211 + (100) - (0.75), 95, 293 + (100) - (0.10), 175,
                                              fill=self.token_color)
        self.canvas.bind('<Button-1>', self.clicked)
        self.canvas.bind('<Motion>', self.callback)
        self.canvas.pack()

        Matrix = [[0 for x in range(6)] for y in range(7)]
        self.game = Grid(self.player1, self.player2, Matrix)
        self.update_top_banner(None, None)

        self.show_scoreboard()

    def show_scoreboard(self):
        self.top_score = tkinter.Frame(master=self.window, width="275", height="50", bg=self.window['bg'])
        self.top_score.place(x=-50, y=10)

        player1_score = self.player1.name.title() + "  " + str(self.player1.wins)
        player2_score = self.player2.name.title() + "  " + str(self.player2.wins)

        player1_score_label = tkinter.Label(master=self.top_score, font=("Helvetica", 18, BOLD), height=1, width=18,
                                            text=player1_score, bg=self.window['bg'])
        player2_score_label = tkinter.Label(master=self.top_score, font=("Helvetica", 18, BOLD), height=1, width=18,
                                            text=player2_score, bg=self.window['bg'])
        player1_score_label.pack()
        player2_score_label.pack()

        # changing top banner according to player turn

    def update_top_banner(self, winner, active):
        print("active is " + str(active))
        if active == False:
            # unbind the token motion and click to restrict player move
            self.canvas.unbind("<Button-1>")
            self.canvas.unbind("<Motion>")

            print("cleared !active is " + str(active))

        self.top = tkinter.Frame(master=self.window, width="1100", height="50", bg=self.window['bg'])
        self.top.place(x=370, y=10)
        if winner != None:
            label_text = winner.name + " has won!"
            player_turn_label = tkinter.Label(master=self.top, font=("Helvetica", 25, BOLD), height=2, width=18,
                                              text=label_text.upper(), fg="#00ace6")
            player_turn_label.pack()
            self.top_score.destroy()
            self.show_scoreboard()

        elif winner == None:
            if self.player1.state == True:
                if self.player1.name[-1] == 's':
                    label_text = self.player1.name.title() + "' turn!"
                else:
                    label_text = self.player1.name.title() + "'s turn!"
            else:
                if self.player1.name[-1] == 's':
                    label_text = self.player2.name.title() + "' turn!"
                else:
                    label_text = self.player2.name.title() + "'s turn!"

            player_turn_label = tkinter.Label(master=self.top, font=("Helvetica", 25, BOLD), height=2, width=18,
                                              text=label_text, bg=self.window['bg'])
            player_turn_label.pack()
        self.show_new_game()


#GUI_Board()