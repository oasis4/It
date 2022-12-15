import tkinter as tk
import winsound
from tkinter import ttk
from rechtecksteuerung2 import *
from winsound import *


class Menu:

    def __init__(self):
        root = tk.Tk()

        root.resizable(False, False)
        root.title('Button Demo')

        # exit button
        game = ttk.Button(root, text='Start', command= self.start)
        weiter = ttk.Button(root, text='Weiter', command= self.weiter)
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

        self.x = 0


        root.mainloop()




    def start(self):

        rl = Rechteck("red", "white")
        rl.R_zeichnen()
        rl.R_bewegen()

    def weiter(self):


        if self.x == 0:
            self.x + 1
            winsound.PlaySound("outro.wav", SND_ASYNC)

        if self.x == 1:
            winsound.PlaySound("hotel.wav", SND_ASYNC)


Menu()