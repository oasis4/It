
from tkinter import *
from time import *
    
#Hier wird eine Klasse mit bestimmten Methoden und Attributen deklariert.
class Tanne:
    def __init__(self, bhintergrund, bfarbe): #Der Konstruktor der Klasse Tanne
        self.hintergrund=bhintergrund       #Attribute der Klasse Tanne
        self.farbe=bfarbe
        self.anzahl=0
 
    def baum_zeichnen(self):    #Methode der Klasse Tanne
        self.root = Tk()
        self.root.title('Frohes Fest!')
        self.bild = Canvas(self.root, background = self.hintergrund, width = 400, height = 400)
        self.bild.pack()
        koordinaten = [160,100,220,160,200,160,260,220,240,220,300,280,20,280,80,220,60,220,120,160,100,160]
        baum=self.bild.create_polygon(koordinaten, outline = 'black', fill = self.farbe)		
        stamm=self.bild.create_rectangle(150, 280, 170, 300, outline = 'black', fill = 'brown')
        self.label=Label(self.root, text='')
        self.label.pack()
        knopfrahmen = Frame(self.root)
        knopfrahmen.pack()
        ende = Button(knopfrahmen, text = 'Ende', command = self.root.destroy)
        ende.pack(side = LEFT)
        self.bild.update()
        #self.root.mainloop()         
 
    def kerzen_anbringen(self):     #Methode der Klasse Tanne
        for i in range (10):
            kerze=self.bild.create_rectangle(60+10*i, 260-15*i, 65+10*i, 265-15*i, outline = 'black', fill = 'red')
            kerze=self.bild.create_rectangle(260-10*i, 260-15*i, 265-10*i, 265-15*i, outline = 'black', fill = 'red')
            sleep(0.2)
            self.bild.update()
        #self.root.mainloop()

    def kerzen_ausblasen(self, anzahl):
        if anzahl < 0 or anzahl > self.anzahl:
            self.label.config(text='So viele Kerzen brennen nicht! Es brennen %d Kerzen.' % self.anzahl)
        else:
            j = 0
            for i in range(int(anzahl / 2)):
                licht = self.bild.create_oval(61 + 10 * j, 257 - 15 * j, 64 + 10 * j, 260 - 15 * j, outline=self.farbe,
                                              fill=self.farbe)
                sleep(0.5)
                j += 1
                self.bild.update()
            j = 0
            for i in range(int(anzahl / 2), anzahl):
                licht = self.bild.create_oval(261 - 10 * j, 257 - 15 * j, 264 - 10 * j, 260 - 15 * j,
                                              outline=self.farbe, fill=self.farbe)
                sleep(0.5)
                j += 1

    def kerzen_anzuenden(self, anzahl):     #Methode der Klasse Tanne
        self.anzahl=anzahl
        if self.anzahl<0 or self.anzahl>20:
            self.label.config(text='Eine solche Kerzenanzahl ist nicht vorhanden!')
        else:
            j=0
            for i in range (int(self.anzahl/2)):
                licht=self.bild.create_oval(61+10*j, 257-15*j, 64+10*j, 260-15*j, fill='yellow')
                sleep(0.2)
                j+=1
                self.bild.update()
            j=0
            for i in range (int(self.anzahl/2), self.anzahl):
                licht=self.bild.create_oval(261-10*j, 257-15*j, 264-10*j, 260-15*j, fill='yellow')
                sleep(0.1)
                j+=1
                self.bild.update()
        #self.root.mainloop()  
  




