from tkinter import *


class Rechteck:
    def __init__(self, koordinaten, farbe, bild, root):
        self.koordinaten=koordinaten
        self.farbe=farbe
        self.root=root
        self.bild=bild
        self.x=0
        self.y=0
    def R_zeichnen(self):
        self.rectangle=self.bild.create_rectangle(self.koordinaten, fill = self.farbe)
        self.root.bind("<KeyPress-Left>", self.R_links_bewegen)
        self.root.bind("<KeyPress-Right>", self.R_rechts_bewegen)
        self.root.bind("<KeyPress-Up>", self.R_aufwaerts_bewegen)
        self.root.bind("<KeyPress-Down>", self.R_abwaerts_bewegen)

    def R_bewegen(self):
        self.bild.move(self.rectangle, self.x, self.y)
        return self.rectangle
    def R_links_bewegen(self, event):
        self.x=-10
        self.y=0
    def R_rechts_bewegen(self, event):
        self.x=10
        self.y=0
    def R_aufwaerts_bewegen(self, event):
        self.x=0
        self.y=-10
    def R_abwaerts_bewegen(self, event):
        self.x=0
        self.y=10

