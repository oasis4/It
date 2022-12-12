
import winsound
from time import *
from tkinter import messagebox
from tkinter import *
class Rechteck:
    winsound.PlaySound("hotel.wav", winsound.SND_ASYNC)

    def __init__(self, farbe, hintergrund):
        self.farbe=farbe


        self.hintergrund = hintergrund
        self.x=1
        self.y=1
        root = Tk()
        root.title('Steuere das Rechteck!')
        self.bild = Canvas(root, background = self.hintergrund, width = 500, height = 500)
        self.bild.pack()
        koordinaten = [180, 160, 210, 250]
        self.rectangle=self.bild.create_rectangle(koordinaten, fill = self.farbe)
        root.bind("<KeyPress-a>", self.R_links_bewegen)
        root.bind("<KeyPress-d>", self.R_rechts_bewegen)
        root.bind("<KeyPress-s>", self.R_abwaerts_bewegen)
        root.bind("<KeyPress-w>", self.R_aufwaerts_bewegen)
        ende = Button(root, text = 'Ende', bg = 'white', fg = 'red', relief = 'sunken', command = root.destroy)
        ende.pack()

        while 1:
            self.bild.move(self.rectangle, self.x, self.y)
            #print(self.bild.coords(self.rectangle))
            if self.bild.coords(self.rectangle)[1]<0 or self.bild.coords(self.rectangle)[3]>500:
                messagebox.showinfo(title='Ende', message='Verloren!!')
                self.bild.destroy()
                break
            elif self.bild.coords(self.rectangle)[0]<0 or self.bild.coords(self.rectangle)[2]>500:
                messagebox.showinfo(title='Ende', message='Verloren!!')
                self.bild.destroy()
                break
            else:
                sleep(0.00001)
                self.bild.update()    
        
    def R_links_bewegen(self, event):
        self.x=-10
        self.y=0
    def R_rechts_bewegen(self, event):
        self.x=10
        self.y=0
    def R_abwaerts_bewegen(self, event):
        self.x=0
        self.y=10
    def R_aufwaerts_bewegen(self, event):
        self.x=0
        self.y=-10
