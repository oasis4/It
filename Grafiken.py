from tkinter import *
from random import *
from time import *
import winsound



class Menu:


    def __init__(self):

        self.root = Tk()
        self.root.title("Menu")
        self.root.resizable(width=False, height=False)
        self.root.config(bg="black")




        b1 = Button(self.root, width = 8, height = 4, fg= "blue", bg= "white", font= ("Courir", "16", "bold"), text = "Klick mich", command= self.start)
        b1.pack()

        #
        self.entry= Entry(self.root, width = 10, fg= "blue", bg= "white", font= ("Courir", "16", "bold"))
        self.entry.pack()
        self.entry.bind("<Return>", self.ausgabe)
        #

        self.label = Label(self.root, width=20, height=7, fg="blue", bg="white", font=("Courir", "16", "bold"), text="")
        self.label.pack()

        self.root.mainloop()


    def zufallszahl(self, x, y):
        a = randint(x, y)
        return a


    def start(self):

        self.label.config(text = "Rate die Zahl von 1 bis 10")
        self.z = self.zufallszahl(0, 10)



    def ausgabe(self, event):

        print(self.z)

        antwort = eval(self.entry.get())
        if antwort == self.z:
            self.label.config(text = "Richtig")
            self.label.config(bg = "green")




        else:
            self.label.config(text = "Falsch")
            self.label.config(bg = "red")



Menu()

