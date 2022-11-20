# Aufgabe 1
for x in range(5):
    print("Hallo")
# Aufgabe 2
a = int(input("Wie oft?:"))
for x in range(a):
    print("Hallo")
# Aufagbe 3
n = int(input("Ganzzahl?:"))
for x in range(n):
    print(x+1)
# Aufgabe 4
n = int(input("Ganzzahl?:"))
for x in range(n):
    print(n-x)
# Aufgabe 5
n = int(input("Ganzzahl?:"))
sol = 0
for x in range(n):
    sol += x+1
print(sol)
# Aufgabe 6
n = int(input("Ganzzahl?:"))
for x in range(n):
    if (((x+1) % 3) == 0):
        print(x+1)
# Aufgabe 7
n = int(input("Ganzzahl?:"))
sol = 0
for x in range(n):
    if (((x+1) % 2) == 0):
        sol += x+1
print(sol)
# Aufgabe 8
n = int(input("Ganzzahl?:"))
sol = 0
for x in range(n):
    if (((x+1) % 2) != 0):
        sol += x+1
print(sol)
# Aufgabe 9
n = int(input("Ganzzahl?:"))
sol = 1
for x in range(n):
    sol *= x+1
print(sol)
# Aufgabe 10
n = int(input("Ganzzahl?:"))
prime = True
for x in range(2, 9):
    if (n % x == 0 and n != x):
        prime = False
        break
if (prime):
    print("Die eingegebene Zahl ist eine Primzahl")
else:
    print("Die eingegebene Zahl ist keine Primzahl")
# Aufgabe 11
inputHöhe = int(input("Höhe?: "))
inputBreite = int(input("Breite?: "))
for i in range(0, inputHöhe):
    for x in range(0, inputBreite):
        print("X", end="")
    print("")
# Aufgabe 12
inputHöhe = int(input("Höhe?: "))
inputBreite = int(input("Breite?: "))
for i in range(0, inputHöhe):
    if (i == 0 or i == inputHöhe-1):
        for x in range(0, inputBreite):
            print("X", end="")
    else:
        print("X", end="")
        for x in range(1, inputBreite-1):
            print(" ", end="")
        print("X", end="")
    print("")
# Aufgabe 12
adjektive = ["rote", "gelbe", "grüne", "blaue", "große", "kleine"]
fruechte = ["Äpfel", "Bananen", "Birnen", "Grapefruits", "Kaktusfeige"]
for x in range(0, len(adjektive)):
    for y in range(0, len(fruechte)):
        if (len(adjektive[x]) < len(fruechte[y]) and adjektive[x][0].lower() != fruechte[y][0].lower()):
            print(adjektive[x], fruechte[y])
