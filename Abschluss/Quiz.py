from time import *
class Quiz:
    print("»»————-　QUIZ　————-««")
    print("Hallo willst ein ein Quiz machen?")
    ja_nein = input()
    if ja_nein == "ja":
        Punkte = 0
        print("Frage 1")
        print("Wie heißt das größte Technologieunternehmen in Südkorea? a = Huawei b = Samsung c = Sony")
        antwort = input()
        sleep(0.5)
        print("...")
        sleep(1)

        if antwort == "b":
            Punkte += 1
            print("Richtig, du bekommst 1 Punkt")
        else:
            print("Leider Falsch")
            Punkte -= 1

        print("2. Frage: Was lange ist die Lebensdauer einer Libelle?")
        print("a = 4 Tage b = 3 Tage c = 1 Tag")
        antwort1 = input()
        sleep(0.5)
        print("...")
        sleep(1)
        if antwort1 == "c":
            print("Das ist richtig")
            Punkte += 1
        else:
            print("Das ist falsch")
            Punkte -= 1
        if Punkte == 1:
            print("Du hast nun", Punkte, "Punkt")
        else:
            print("Du hast nun", Punkte, "Punkte")
        print("3. Frage: Wie viele Atemzüge nimmt der menschliche Körper täglich? ")
        print("a = 10.000 b = 20.000 c = 30.000")
        antwort2 = input()
        sleep(0.5)
        print("...")
        sleep(1)
        if antwort2 == "b":
            print("Das ist richtig")
            Punkte += 1
            if Punkte == 1:
                print("Du hast nun", Punkte, "Punkt")
            else:
                print("Du hast nun", Punkte, "Punkte")
        else:
            print("Das ist falsch")

            Punkte -= 1

        print("Vielen Dank, dass du mitgemacht hast")
        print("Du hast:")
        sleep(0.5)
        print("...")
        sleep(1)
        print("...")
        sleep(1)
        if Punkte == 1:
            print("Du hast nun", Punkte, "Punkt")
        else:
            print("Du hast nun", Punkte, "Punkte")

    else:
        print("Schade ¯\_(ツ)_/¯")


