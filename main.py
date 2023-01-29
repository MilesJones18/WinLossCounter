import tkinter as tk
from tkinter import ttk
from tkinter import *

root = tk.Tk()
root.title('Win/Loss')
root.geometry('600x400+50+50')
root.resizable(False, False)

wins = 0
losses = 0


def click():
    label.config(text=wins)


def click2():
    label2.config(text=losses)


def button_add():
    global wins
    wins += 1
    if wins > 7:
        wins = 0
    print(wins)


def button_addloss():
    global losses
    global wins
    losses += 1
    if losses > 20:
        wins = 0
        losses = 0
    print(losses)


def button_subtract():
    global wins
    wins -= 1
    if wins < 0:
        wins = 0
    print(wins)


def button_subtractloss():
    global losses
    losses -= 1
    if losses < 0:
        losses = 0
    print(losses)


def button_resets():
    global wins
    global losses
    wins = 0
    losses = 0
    print(wins)


label = Label(root,
              text=wins,
              font=("System", 24),
              borderwidth=1,
              relief="solid"
              )

label2 = Label(root,
               text=losses,
               font=("System", 24),
               borderwidth=1,
               relief="solid"
               )

Wins = Label(root,
             text="Wins",
             font=("System", 28)
             )

Losses = Label(root,
               text="Losses",
               font=("System", 28),
               )

add_button = ttk.Button(
    root,
    text="+1",
    compound=tk.LEFT,
    command=lambda: [button_add(), click()]
)

addloss_button = ttk.Button(
    root,
    text="+1",
    compound=tk.LEFT,
    command=lambda: [button_addloss(), click2()]
)

minus_button = ttk.Button(
    root,
    text="-1",
    compound=tk.RIGHT,
    command=lambda: [button_subtract(), click()]
)

minusloss_button = ttk.Button(
    root,
    text="-1",
    compound=tk.RIGHT,
    command=lambda: [button_subtractloss(), click2()]
)

label.place(x=110, y=80, height=50, width=100)
label2.place(x=390, y=80, height=50, width=100)
Wins.place(x=105, y=25, )
Losses.place(x=370, y=25)

add_button.place(x=110, y=200, height=50, width=100)
minus_button.place(x=110, y=250, height=50, width=100)
addloss_button.place(x=390, y=200, height=50, width=100)
minusloss_button.place(x=390, y=250, height=50, width=100)
root.mainloop()
