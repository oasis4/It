from time import *
from random import *

def Zufallszahl(x,y):
    z=randint(x,y)
    return z

def Zufallsfarbe(rot,schwarz):
    f=randint(rot,schwarz)
    return f


zahl = Zufallszahl(0,36)
farbe = Zufallsfarbe(1,2)

if farbe == 1:
    farbe = "schwarz"
else:
    farbe = "rot"

while True:
    print("𝓦𝓲𝓵𝓵𝓴𝓸𝓶𝓶𝓮𝓷 𝔃𝓾𝓶 𝓡𝓸𝓾𝓵𝓮𝓽𝓽𝓮")
    print("Auf was willst du Setzen? 1 = Zahl oder 2 = Farbe")
    farbe_zahl = input()
    if farbe_zahl == "1":
        print("Du willst auf die richtige Zahl gehen.")
        print("Gib bitte eine Zahl zwischen 1 und 36 ein:")
        spzahl = input()
        print("Du hast die " + spzahl + " ausgewählt")



    else:
        print("Du willst auf die richtige Farbe gehen.")
        print("Gib bitte jetzt deine Farbe ein")
        print("Rot oder Schwarz")
        spfarbe = input()
        print("Du hast " + spfarbe + " ausgewählt")
        print("Die Kugel ist unterwegs")
        sleep(1)
        print(".....")
        sleep(1)
        print("Oh")
        sleep(1)
        print(".....")
        print("Es ist " + farbe)
        if farbe == farbe_zahl:
            print("Richig")
        else:
            print("schade")







