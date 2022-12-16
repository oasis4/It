import tkinter as tk
import winsound
from tkinter import ttk
from rechtecksteuerung2 import *
from winsound import *
from random import *


def Zufallszahl(x, y):
    z = randint(x, y)
    return z

def start():

    rl = Rechteck("red")
    rl.R_zeichnen()
    rl.R_bewegen()


class Menu:

    def __init__(self):
        root = tk.Tk()

        root.resizable(False, False)
        root.title('GAME')

        game = ttk.Button(root, text='Start', command=start)
        weiter = ttk.Button(root, text='Musik', command = self.weiter,)
        stop = ttk.Button(root, text='Exit', command=root.destroy)



        game.pack(
            ipadx=5,
            ipady=5,
            expand=True
        )
        weiter.pack(
            ipadx=5,
            ipady=5,
            expand=True
        )

        stop.pack(
            ipadx=5,
            ipady=5,
            expand=True
        )

        self.zahl = Zufallszahl(1, 4)

        root.mainloop()

    def weiter(self):

        print(self.zahl)

        if self.zahl == 1:
            winsound.PlaySound("outro.wav", SND_ASYNC)

        elif self.zahl == 2:

            winsound.PlaySound("hotel.wav", SND_ASYNC)

        elif self.zahl == 3:

            winsound.PlaySound("Be MY Lover.wav", SND_ASYNC)
        else:
            winsound.PlaySound("Waka Waka.wav", SND_ASYNC)


Menu()
