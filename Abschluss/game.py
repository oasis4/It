import tkinter as tk
from rechtecksteuerung2 import *
from winsound import *
from random import *
from PIL import Image, ImageTk

def gf():
    menu = Menu()
    menu.start()

def qz():
    import Quiz

    qz = Quiz()
    qz.start()

class Menu:

    def __init__(self):
        self.root = Tk()
        self.root.focus_force()
        self.root.resizable(False, False)
        self.root.focus_force()
        self.root.iconbitmap('favicon.ico')


        self.time = 0.05

        self.root.title('Menu')

        image = Image.open("hintergrund.jpg")
        image = image.resize((290, 200), Image.ANTIALIAS)
        pic = ImageTk.PhotoImage(image)

        self.canvas = Canvas(self.root, width=400, height=300)

        self.hintergrund = PhotoImage(file='hintergrund.ppm')


        self.canvas.create_image(200, 150, image=pic, anchor=CENTER)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        game = Button(self.root,width=10,height=1, text='Spiel',  command=self.start)

        quiz = Button(self.root,width=10,height=1, text='Quiz',  command=qz)

        grafik = Button(self.root,width=10,height=1, text='Zahlenraten',  command=gf)

        weiter = Button(self.root,width=10,height=1, text='Musik',  command=self.weiter)

        stop = Button(self.root, text='Exit',  command=self.root.destroy)

        #Hover
        self.Hover(game, "SkyBlue2", "white")
        self.Hover(quiz, "SkyBlue2", "white")
        self.Hover(grafik, "SkyBlue2", "white")
        self.Hover(weiter, "SkyBlue2", "white")
        self.Hover(stop, "red", "white")


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
        self.canvas.create_window(320, 230, window=stop)

        #image Button
        einstellungimg = PhotoImage(file='einstellungen.png')

        einstellungbutton = Button(self.root, image=einstellungimg, width=70, height=70, command=self.createNewWindow, borderwidth=0)
        einstellungbutton.pack(pady=30)
        einstellungbutton.place(x=280, y=40)

        self.root.mainloop()

        # Hover Animation

    def Hover(self,button, colorOnHover, colorOnLeave):

        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover))

        button.bind("<Leave>", func=lambda e: button.config(
            background=colorOnLeave))

    def start(self):
        rl = Rechteck("red", "white", self.time)
        rl.R_zeichnen()
        rl.R_bewegen()

    def createNewWindow(self):
        self.newWindow = tk.Toplevel(self.root)
        Text = tk.Label(self.newWindow, text="Wähle die Schwierigkeit")
        einfach = tk.Button(self.newWindow, text="einfach", command=self.einfach)
        normal = tk.Button(self.newWindow, text="normal", command=self.normal)
        schwer = tk.Button(self.newWindow, text="schwer", command=self.schwer)

        Text.pack()
        einfach.pack()
        normal.pack()
        schwer.pack()

    def einfach(self):
        self.time = 0.05
        self.newWindow.destroy()

    def normal(self):
        self.time = 0.02
        self.newWindow.destroy()

    def schwer(self):
        self.time = 0.01
        self.newWindow.destroy()

    def weiter(self):

        def Zufallszahl(x, y):
            z = randint(x, y)
            return z

        self.zahl = Zufallszahl(1, 4)

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
