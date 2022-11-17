import math
# Aufgabe 1
userInput = input("Ganzzahl?")
match userInput:
    case "1":
        print("sehr gut")
    case "2":
        print("gut")
    case "3":
        print("befriedigend")
    case "4":
        print("ausreichend")
    case "5":
        print("mangelhaft")
    case "6":
        print("ungenügend")
    case _:
        print("Fehler")
# Aufgabe 2
userInputOne = int(input("Erste Zahl?"))
userInputTwo = int(input("Zweite Zahl?"))
if (userInputOne >= 0 and userInputTwo >= 0):
    if (userInputOne > userInputTwo and userInputTwo != 0):
        print(userInputOne/userInputTwo, "a")
    elif (userInputOne < userInputTwo and userInputOne != 0):
        print(userInputTwo/userInputOne, "b")
    else:
        print("Fehler")
else:
    print("Fehler")
# Aufgabe 3
a = int(input("Geben Sie eine Niederschlagsmenge ein:"))
b = int(input("Geben Sie eine Niederschlagsmenge ein:"))
c = int(input("Geben Sie eine Niederschlagsmenge ein:"))
max = a
if (max < b):
    max = b
if (max < c):
    max = c
min = a
if (min > b):
    min = b
if (min > c):
    min = c
print("Die größte der eingegebenen Niederschlagsmenge ist", max,
      "und die kleinste der eingegebenen Niederschlagsmenge ist", min)
# Aufgabe 4
array = []
array.append(int(input("Zahl?: ")))
array.append(int(input("Zahl?: ")))
array.append(int(input("Zahl?: ")))
array.sort()
print(array)
# Aufgabe 5
userInputOne = int(input("Erste Zahl?"))
userInputTwo = int(input("Zweite Zahl?"))
userInput = int(input("Was soll mit den Zahlen gemacht werden?"))
match userInput:
    case "1":
        print(userInputOne+userInputTwo)
    case "2":
        print(userInputOne-userInputTwo)
    case "3":
        print(userInputOne*userInputTwo)
    case "4":
        print(userInputOne/userInputTwo)
    case "5":
        print(userInputOne//userInputTwo)
    case "6":
        print(userInputOne % userInputTwo)
    case "7":
        print(userInputOne ** userInputTwo)
    case _:
        print("Fehler")
# Aufgabe 6
userInput = int(input("Jahr?"))
schaltjahre = True
if (userInput % 4):
    schaltjahre = False
    if (userInput/100):
        schaltjahre = True
        if (userInput/400):
            schaltjahre = False
if (schaltjahre):
    print(userInput, "Ist ein Schaltjahr")
else:
    print(userInput, "Ist kein Schaltjahr")
# Aufgabe 7
userInput = int(input("Wie viele Fahrten?"))
ohne = userInput*5
bahn25 = 50+(3.75*userInput)
bahn50 = 200+(2.5*userInput)
print(userInput, "Fahrten kosten ohne Bahncard", ohne,
      "€ mit Bahncard25", bahn25, "€ und mit Bahncard50", bahn50, "€")
if (ohne < bahn25 and ohne < bahn50):
    print("Für die gewählten", userInput,
          "Fahrten ist weder der Kauf einer Bahncard50 noch einer Bahncard25 sinnvoll.")
if (bahn25 < ohne and bahn25 < bahn50):
    print("Bahncard25 ist am sinnvollsten")
if (bahn50 < ohne and bahn50 < bahn25):
    print("Bahncard50 ist am sinnvollsten")
# Aufgabe 8:
a = 0
while (a == 0):
    a = int(input("A?: "))
b = 0
c = 0
while (b == 0 and c == 0):
    b = int(input("B?: "))
    c = int(input("C?: "))
b = +(b/a)
c = -(c/a)
p = -(b/2)
q = math.sqrt(((b/2)**2)-(c))
print(p + q)
print(p - q)
