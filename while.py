import random
# Aufgabe 1 – Wiederholte Codeausführung
count = 1
while (count <= 5):
    print(count)
    count += 1
# Aufgabe 2 – Wiederholte Begrüßung
hey = int(input("Wie oft Hallo?"))
while (hey != 0):
    print("Hallo")
    hey -= 1
# Aufgabe 3 – Summieren bis Hundert
inputUser = 0
while (inputUser <= 100):
    inputUser = int(input("Number?"))
# Aufgabe 4 – Hauptstädte der Bundesländer
finish = False
while (finish == False):
    bundesland = input("Bundesland?: ")
    match bundesland:
        case "Ende":
            finish = True
        case "Baden-Württemberg":
            print("Stuttgart")
        case "Bayern":
            print("München")
        case "Berlin":
            print("Berlin")
        case "Brandenburg":
            print("Potsdam")
        case "Bremen":
            print("Bremen")
        case "Hamburg":
            print("Hamburg")
        case "Hessen":
            print("Wiesbaden")
        case "Mecklenburg-Vorpommern":
            print("Schwerin")
        case "Niedersachsen ":
            print("Hannover")
        case "Nordrhein-Westfalen":
            print("Düsseldorf")
        case "Saarland ":
            print("Saarbrücken")
        case "Sachsen":
            print("Dresden")
        case "Sachsen-Anhalt":
            print("Magdeburg")
        case "Schleswig-Holstein ":
            print("Kiel")
        case "Thüringen":
            print("Erfurt")
        case _:
            print("„Falsche Eingabe“")
# Aufgabe 5 – Zahlenraten
meineZufallszahl = random.randint(0, 100)
userNumber = 101
while (meineZufallszahl != userNumber):
    userNumber = int(input("Deine Nummer?: "))
    if (userNumber > meineZufallszahl):
        print("Die Nummer ist kleiner")
    if (userNumber < meineZufallszahl):
        print("Die Nummer ist größer")
    if (userNumber < 0):
        break
    if (meineZufallszahl == userNumber):
        print("GG WP!")
# Aufgabe 6 – Notenschnitt
finish = False
noten = 0
count = 0
while (finish != True):
    inputUser = input("Note?")
    if (inputUser == "Ende"):
        finish = True
        break
    if (inputUser > 0 and inputUser > 7):
        noten += (int(inputUser))
        count += 1
    else:
        print("Keine Gültige Schulnote")
print(noten/count)
# Aufgabe 7 – Verschachtelte Schleifen
inputHöhe = int(input("Höhe?: "))
inputBreite = int(input("Breite?: "))
counthöhe = 0
while (counthöhe < inputHöhe):
    counthöhe += 1
    countbreite = 0
    while (countbreite < inputBreite):
        countbreite += 1
        print("X", end="")
    print("")
# Aufgabe 8 – Verschachtelte Schleifen
inputHöhe = int(input("Höhe?: "))
inputBreite = int(input("Breite?: "))
i = 0
while (i < inputHöhe):

    if (i == 0 or i == inputHöhe-1):
        for x in range(0, inputBreite):
            print("X", end="")
    else:
        for x in range(0, inputBreite):
            if (x != 0 and x != inputBreite-1):
                print(" ", end="")
            else:
                print("X", end="")
    print("")
    i += 1
