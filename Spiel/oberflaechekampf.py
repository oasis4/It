from tkinter import *
from rechteck import *
from oval import *
from time import *
from tkinter import messagebox

class Oberflaechekampf:
    def __init__(self, hintergrund):
        self.hintergrund=hintergrund
        self.root = Tk()
        self.root.title('Oberfläche')
        self.bild = Canvas(self.root, background = self.hintergrund, width = 500, height = 500)
        self.bild.pack()
        ende = Button(self.root, text = 'Ende', bg = 'white', fg = 'red', relief = 'sunken', command = self.root.destroy)
        ende.pack()
        self.r=Rechteck([180, 160, 210, 250], 'blue', self.bild, self.root)
        self.r.R_zeichnen()
        self.o=Oval([300,350,400,470], 'green', self.bild, self.root)
        self.o.O_zeichnen()
    def bewegen(self):
        rbild=self.r.R_bewegen()
        #print('Rechteck', self.bild.coords(rbild))
        obild=self.o.O_bewegen()
        #print('Oval', self.bild.coords(obild))
        if self.bild.coords(rbild)[0]<0 or self.bild.coords(rbild)[2]>500:
            self.bild.delete(rbild)
            messagebox.showinfo(title='Ende', message='Verlierer: Rechteck!!')
            self.stop()
        elif self.bild.coords(rbild)[1]<0 or self.bild.coords(rbild)[3]>500:
            self.bild.delete(rbild)
            messagebox.showinfo(title='Ende', message='Verlierer: Rechteck!!')
            self.stop()
        elif self.bild.coords(obild)[0]<0 or self.bild.coords(obild)[2]>500:
            self.bild.delete(obild)
            messagebox.showinfo(title='Ende', message='Verlierer: Oval!!')
            self.stop()
        elif self.bild.coords(obild)[1]<0 or self.bild.coords(obild)[3]>500:
            self.bild.delete(obild)
            messagebox.showinfo(title='Ende', message='Verlierer: Oval!!')
            self.stop()
        elif ((self.bild.coords(rbild)[0]>self.bild.coords(obild)[0] and self.bild.coords(rbild)[0]<self.bild.coords(obild)[2]) and (self.bild.coords(rbild)[1]>self.bild.coords(obild)[1] and self.bild.coords(rbild)[1]<self.bild.coords(obild)[3])):
            self.bild.delete(rbild)
            messagebox.showinfo(title='Ende', message='Verlierer: Rechteck!!')
            self.stop()
        elif ((self.bild.coords(obild)[0]>self.bild.coords(rbild)[0] and self.bild.coords(obild)[0]<self.bild.coords(rbild)[2]) and (self.bild.coords(obild)[1]>self.bild.coords(rbild)[1] and self.bild.coords(obild)[1]<self.bild.coords(rbild)[3])):
            self.bild.delete(obild)
            messagebox.showinfo(title='Ende', message='Verlierer: Oval!!')
            self.stop()
        else:
            sleep(0.05)
            self.bild.update()
            self.bewegen()
    def stop(self):
        sleep(1)
        self.root.destroy()
        
        
