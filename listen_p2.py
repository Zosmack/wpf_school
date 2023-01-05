# Diese Funktion addiert alle Zahlen einer Liste und gibt die Summe zurück
import copy


def summiereAlleZahlenInListe(liste):
    zwischensumme = 0
    for zahl in liste:
        zwischensumme = zwischensumme + zahl
    return zwischensumme


# Diese Funktion ermittelt die größte Zahl einer Liste und gibt diese zurück
def ermittleGroessteZahlInListe(liste):
    bisherGroessteZahl = liste[0]
    for zahl in liste:
        if zahl > bisherGroessteZahl:
            bisherGroessteZahl = zahl
    return bisherGroessteZahl


# Aufgabe 1
def multipliziereAlleZahlenInListe(liste):
    if (len(liste) != 0):
        sol = 1
        for num in liste:
            sol *= num
        return sol
    else:
        return 0


# Aufgabe 2
def ermittleKleinsteZahlInListe(liste):
    listecopy = liste.copy()
    listecopy.sort()
    return (listecopy[0])


# Aufgabe 3
def istListeLeer(liste):
    if (len(liste) != 0):
        return False
    else:
        return True


# Aufgabe 4
def ermittleIndexDerKleinstenZahl(liste):
    listecopy = liste.copy()
    listecopy.sort()
    return liste.index(listecopy[0])


# Aufgabe 5
def gibVerdoppelteListeZurueck(liste):
    listecopy = []
    for number in liste:
        listecopy.append(number*2)
    return listecopy


# Aufgabe 6
def zaehleZweistelligeZahlen(liste):
    count = 0
    for number in liste:
        if (number >= 10 and number <= 99):
            count += 1
    return count


# Aufgabe 7
def entferneGeradeZahlen(liste):
    listecopy = []
    for number in liste:
        if (number % 2 != 0):
            listecopy.append(number)
    return listecopy


# Aufgabe 8
def sindAlleZahlenPositv(liste):
    for number in liste:
        if (number < 0):
            return False
    return True


# Aufgabe 9
def mehrPositiveoderNegativeZahlen(liste):
    countPositive = 0
    countNegative = 0
    for number in liste:
        if (number < 0):
            countNegative += 1
        else:
            countPositive += 1
    if (countPositive > countNegative):
        return "Die Liste hat mehr positive als negative Zahlen"
    else:
        return "Die Liste hat mehr negative als positive Zahlen"


# Unsere Beispielzahlenliste
zahlenliste = [5, 2, 9, 13, 16, 27, 1, 67, 12, 56]
# Nun testen wir beide Funktionen mit unserer Beispielliste
summeDerZahlenliste = summiereAlleZahlenInListe(zahlenliste)
print("Die Summe aller Zahlen in der Zahlenliste ist ", summeDerZahlenliste)
groessteZahlInZahlenliste = ermittleGroessteZahlInListe(zahlenliste)
print("Die größte Zahl in der Zahlenliste ist ", str(groessteZahlInZahlenliste))
print(multipliziereAlleZahlenInListe(zahlenliste))
print(ermittleKleinsteZahlInListe(zahlenliste))
print(istListeLeer(zahlenliste))
print(istListeLeer(zahlenliste))
print(ermittleIndexDerKleinstenZahl(zahlenliste))
print(gibVerdoppelteListeZurueck(zahlenliste))
print(zaehleZweistelligeZahlen(zahlenliste))
print(entferneGeradeZahlen(zahlenliste))
print(sindAlleZahlenPositv(zahlenliste))
print(mehrPositiveoderNegativeZahlen(zahlenliste))
print(1, "s")
