#!/usr/bin/env python3

# Guess the number (Computer) using an tkinter GUI
# Based on FreeCodeCamp.org
# John Diaz january 2023
# TO DO List:
#

import random
from tkinter import *

root = Tk()
root.option_add( "*font", "lucida 23 bold " )
box = Entry(root, width=40, borderwidth=7, bg="white", fg="black")
box.pack()

# Initialize the number to be guess
limit = random.randint(10, 100)
number = random.randint(1, limit)

root.title(f" Enter a number between 0 and {limit}")


def btn_func():
    # Get the number in the box and substract with the actual number
    x = int(box.get()) - number
    if x == 0:
        btnLabel = Label(root, text=box.get() + " is the right number!!!")
    elif x > 0:
        btnLabel = Label(root, text=box.get() + " is too high...")
    elif x < 0:
        btnLabel = Label(root, text=box.get() + " is too low...")
    btnLabel.pack()
    # Clean the box
    box.delete(0, END)


btn = Button(root, text=" Check you guess !!!", command=btn_func)
btn.pack()


root.mainloop()
