"""
Joonas Karhumaa
karhumaa.joonas@gmail.com

Classic 4x4 memory game with electrician tools
and elements theme. Icons made by Freepik from
www.flaticon.com
"""

from tkinter import *
from tkinter import messagebox
from random import shuffle
import sys
import os

class UserInterface:
    
    def __init__(self):
        # creating main windonw and adding the title
        self.__root = Tk()
        self.__root.title("Muistipeli")

        # defining images as objects
        self.__screwdriver_pic = PhotoImage(file = "screwdriver.png")
        self.__handdrill_pic = PhotoImage(file = "handdrill.png")
        self.__flashlight_pic = PhotoImage(file = "flashlight.png")
        self.__lightbulb_pic = PhotoImage(file = "lightbulb.png")
        self.__wires_pic = PhotoImage(file ="wires.png")
        self.__plug_pic = PhotoImage(file = "plug.png")
        self.__accumulator_pic = PhotoImage(file = "accumulator.png")
        self.__danger_pic = PhotoImage(file = "danger.png")
        self.__bg_pic = PhotoImage(file = "background.png")

        # initializing variables which are used later in the program
        self.__click_count = 0
        self.__button_list = []
        self.__answer_list = []

        # adding pictures to a list so that they can be easily randomized
        self.__picture_list = [self.__screwdriver_pic, self.__screwdriver_pic,
                                self.__handdrill_pic, self.__handdrill_pic,
                                self.__flashlight_pic, self.__flashlight_pic,
                                self.__lightbulb_pic, self.__lightbulb_pic,
                                self.__wires_pic, self.__wires_pic,
                                self.__plug_pic, self.__plug_pic,
                                self.__accumulator_pic, self.__accumulator_pic,
                                self.__danger_pic, self.__danger_pic]
        # randomizing pictures
        shuffle(self.__picture_list)

        # creating start and stop buttons
        self.__start_button = Button(self.__root, text = "Uusi peli",
                                    command = self.new_game)
        self.__stop_button = Button(self.__root, text = "Lopeta peli",
                                    command = self.stop)

        # creating buttons for cards
        self.__button1 = Button(self.__root, image = self.__bg_pic,
                                height=130, width=130, command=lambda:
                                self.turn_card(self.__button1, 0))
        self.__button2 = Button(self.__root, image = self.__bg_pic,
                                height=130, width=130, command=lambda:
                                self.turn_card(self.__button2, 1))
        self.__button3 = Button(self.__root, image = self.__bg_pic,
                                height=130, width=130, command=lambda:
                                self.turn_card(self.__button3, 2))
        self.__button4 = Button(self.__root, image = self.__bg_pic,
                                height=130, width=130, command=lambda:
                                self.turn_card(self.__button4, 3))

        self.__button5 = Button(self.__root, image = self.__bg_pic,
                                height=130, width=130, command=lambda:
                                self.turn_card(self.__button5, 4))
        self.__button6 = Button(self.__root, image = self.__bg_pic,
                                height=130, width=130, command=lambda:
                                self.turn_card(self.__button6, 5))
        self.__button7 = Button(self.__root, image = self.__bg_pic,
                                height=130, width=130, command=lambda:
                                self.turn_card(self.__button7, 6))
        self.__button8 = Button(self.__root, image = self.__bg_pic,
                                height=130, width=130, command=lambda:
                                self.turn_card(self.__button8, 7))

        self.__button9 = Button(self.__root, image = self.__bg_pic,
                                height=130, width=130, command=lambda:
                                self.turn_card(self.__button9, 8))
        self.__button10 = Button(self.__root, image = self.__bg_pic, 
                                height=130, width=130, command=lambda:
                                self.turn_card(self.__button10, 9))
        self.__button11 = Button(self.__root, image = self.__bg_pic,
                                height=130, width=130, command=lambda:
                                self.turn_card(self.__button11, 10))
        self.__button12 = Button(self.__root, image = self.__bg_pic,
                                height=130, width=130, command=lambda:
                                self.turn_card(self.__button12, 11))

        self.__button13 = Button(self.__root, image = self.__bg_pic,
                                height=130, width=130, command=lambda:
                                self.turn_card(self.__button13, 12))
        self.__button14 = Button(self.__root, image = self.__bg_pic,
                                height=130, width=130, command=lambda:
                                self.turn_card(self.__button14, 13))
        self.__button15 = Button(self.__root, image = self.__bg_pic,
                                height=130, width=130, command=lambda:
                                self.turn_card(self.__button15, 14))
        self.__button16 = Button(self.__root, image = self.__bg_pic,
                                height=130, width=130, command=lambda:
                                self.turn_card(self.__button16, 15))

        # placing buttons in the main window
        self.__start_button.grid(row=0, column=2)
        self.__stop_button.grid(row=0, column=3)

        self.__button1.grid(row=1, column=1)
        self.__button2.grid(row=1, column=2)
        self.__button3.grid(row=1, column=3)
        self.__button4.grid(row=1, column=4)

        self.__button5.grid(row=2, column=1)
        self.__button6.grid(row=2, column=2)
        self.__button7.grid(row=2, column=3)
        self.__button8.grid(row=2, column=4)

        self.__button9.grid(row=3, column=1)
        self.__button10.grid(row=3, column=2)
        self.__button11.grid(row=3, column=3)
        self.__button12.grid(row=3, column=4)

        self.__button13.grid(row=4, column=1)
        self.__button14.grid(row=4, column=2)
        self.__button15.grid(row=4, column=3)
        self.__button16.grid(row=4, column=4)
    

    def turn_card(self, button, number):
        """
        Method for turning over cards. When two cards are turned method
        checks if the picked cards are the same.

        :param button: object, button which is clicked
        :paran number: int, number for choosing the picture to card
                        from randomized picture list
        """
        if self.__click_count < 2:

            # chancing picture to the pressed card and disabling the button
            # so that the same button cannot be pressed more than once
            button.configure(image = self.__picture_list[number])
            button["state"] = DISABLED

            # adding the pressed button to the list and the picture in
            # the card to another list
            self.__button_list.append(button)
            self.__answer_list.append(button["image"])
            self.__click_count += 1

        else:

            # if pictures in the answer list are the same cards are a pair
            if self.__answer_list[0] == self.__answer_list[1]:
                # resetting the lists and clicker counter
                self.__click_count = 0
                self.__answer_list = []
                self.__button_list = []

            else:
                # turning the buttons over if they aren't a pair
                for button in self.__button_list:
                    self.turn_over(button)

                # resetting the lists and clicker counter
                self.__answer_list = []
                self.__button_list = []
                self.__click_count = 0 
              

    def turn_over(self, button):
        """
        Method for turning over cards if they are not a pair.
        Method also returns the button state to normal.
        """
        button.configure(image = self.__bg_pic)
        button["state"] = NORMAL

    def stop(self):
        """
        Stops the execution of the program.
        """
        answer = messagebox.askquestion(title=None, message="Haluatko varmasti lopettaa pelin?")

        if answer == "yes":
            self.__root.destroy()

    def new_game(self):
        """
        Starts new game.
        """
        answer = messagebox.askquestion(title=None, message="Haluatko varmasti aloittaa uuden pelin?")

        if answer == "yes":
            python = sys.executable
            os.execl(python, python, * sys.argv)

    def start(self):
        """
        Starts the user interface with the mainloop.
        """
        self.__root.mainloop()

def main():

    # Starting the user interface.
    ui = UserInterface()
    ui.start()

if __name__ == "__main__":
    main()
