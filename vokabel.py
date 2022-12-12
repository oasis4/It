import winsound
from random import *
from time import *


vokabeln=[("Alles Klar", "alright"), ("Gesundheit" , "Bless you!"), ("blau", "blue")]
for i in range( len (vokabeln)):
    print("Deutsch: ")
    x = randint(0, len (vokabeln)-1)
    print(vokabeln[x][0])
    print("Englische Übersetzung eingeben:")
    a = input()
    if a == vokabeln[i][1]:
        print("Richtig")

    else:
        print("Falsch")
        print("Es ist " + vokabeln[i][1])
        winsound.PlaySound("falsch", winsound.SND_ALIAS)



sleep(1)
winsound.PlaySound("outro", winsound.SND_ALIAS)
sleep(18)
print("ENDE")