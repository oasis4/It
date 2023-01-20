
from tkinter import *

class Tanneerb:
    def __init__(self):
        self.root = Tk()
        game = Button(self.root, width=10, height=1, text='Spiel', command=self.start)

        game.pack(
            ipadx=5,
            ipady=5,
            expand=True
        )

    def start(self):
        from tannenbaum import Tanne
        o = Tanne(bhintergrund="yellow", bfarbe="green")

        o.baum_zeichnen()
        o.kerzen_anbringen()
        o.kerzen_anzuenden(anzahl=20)
        o.kerzen_ausblasen(anzahl=20)












