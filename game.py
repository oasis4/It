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
    rl = Rechteck("red", "white")
    rl.R_zeichnen()
    rl.R_bewegen()



def gf():
    import Grafiken

    menu = Menu()
    menu.start()

def qz():
    import Quiz

    qz = Quiz()
    qz.start()

class Menu:

    def __init__(self):
        root = Tk()
        root.focus_force()
        root.resizable(False, False)


        root.title('GAME')

        self.canvas = Canvas(root, width=400, height=300)
        self.hintergrund = PhotoImage(file='hintergrund.ppm')
        self.canvas.create_image(200, 150, image=self.hintergrund)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        game = ttk.Button(root, text='Start', command=start)

        quiz = ttk.Button(root, text='Quiz', command=qz)

        grafik = ttk.Button(root, text='Zahlenraten', command=gf)

        weiter = ttk.Button(root, text='Musik', command=self.weiter)

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
        quiz.pack(
            ipadx=5,
            ipady=5,
            expand=True
        )
        grafik.pack(
            ipadx=5,
            ipady=5,
            expand=True
        )

        self.canvas.create_window(100, 80, window=game)
        self.canvas.create_window(100, 120, window=grafik)
        self.canvas.create_window(100, 160, window=quiz)
        self.canvas.create_window(100, 200, window=weiter)

        self.canvas.create_window(300, 230, window=stop)

        self.zahl = Zufallszahl(1, 4)

        root.mainloop()

    def weiter(self):

        print(self.zahl)

        if self.zahl == 1:
            winsound.PlaySound("feeling.wav", SND_ASYNC)

        elif self.zahl == 2:

            winsound.PlaySound("animals.wav", SND_ASYNC)

        elif self.zahl == 3:

            winsound.PlaySound("Be MY Lover.wav", SND_ASYNC)
        else:
            winsound.PlaySound("Waka Waka.wav", SND_ASYNC)


Menu()
