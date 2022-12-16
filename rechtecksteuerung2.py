
import winsound
from time import *
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
class Rechteck:


    def __init__(self, hintergrundfarbe):
        self.farbe= hintergrundfarbe



        self.x=1
        self.y=1
        root = Tk()

        img = PhotoImage(file="TEST.png")
        Label = ttk.Label(root, image=img)
        Label.pack()
        self.hintergrund = img

        root.title('Steuere das Rechteck!')
        self.bild = Canvas(root, width = 500, height = 500)
        self.bild.pack()

        self.bild.create_image(10, 10, anchor=NW, image=img)

        koordinaten = [180, 160, 210, 250]
        self.rectangle = self.bild.create_rectangle(koordinaten, fill=self.farbe)
        root.bind("<KeyPress-a>", self.R_links_bewegen)
        root.bind("<KeyPress-d>", self.R_rechts_bewegen)
        root.bind("<KeyPress-s>", self.R_abwaerts_bewegen)
        root.bind("<KeyPress-w>", self.R_aufwaerts_bewegen)
        stop = ttk.Button(root, text='Stop', command=root.destroy)
        stop.pack()

        while 1:
            self.bild.move(self.rectangle, self.x, self.y)
            #print(self.bild.coords(self.rectangle))
            if self.bild.coords(self.rectangle)[1]<0 or self.bild.coords(self.rectangle)[3]>500:
                messagebox.showinfo(title='Ende', message='Verloren!!')
                self.bild.destroy()
                break
            elif self.bild.coords(self.rectangle)[0]<0 or self.bild.coords(self.rectangle)[2]>500:
                self.bild.destroy()
                break
            else:
                sleep(0.01)
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
