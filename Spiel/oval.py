from tkinter import *


class Oval:
    def __init__(self, koordinaten, farbe, bild, root):
        self.koordinaten=koordinaten
        self.farbe=farbe
        self.root=root
        self.bild=bild
        self.v=0
        self.w=0
    def O_zeichnen(self):
        self.oval=self.bild.create_oval(self.koordinaten, fill = self.farbe)
        self.root.bind("<KeyPress-a>", self.O_links_bewegen)
        self.root.bind("<KeyPress-d>", self.O_rechts_bewegen)
        self.root.bind("<KeyPress-w>", self.O_aufwaerts_bewegen)
        self.root.bind("<KeyPress-s>", self.O_abwaerts_bewegen)
        
    def O_bewegen(self):
        self.bild.move(self.oval, self.v, self.w)
        return self.oval
            
    def O_links_bewegen(self, event):
        self.v=-10
        self.w=0
    def O_rechts_bewegen(self, event):
        self.v=10
        self.w=0
    def O_abwaerts_bewegen(self, event):
        self.v=0
        self.w=10
    def O_aufwaerts_bewegen(self, event):
        self.v=0
        self.w=-10
