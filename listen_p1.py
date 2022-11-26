# Aufgabe 1
schuelernamen = ["Jan", "Max", "Fabian"]
print(schuelernamen)
for name in schuelernamen:
    print(name)

schuelernamen.count("Jan")
schuelernamen.append("Tom")
schuelernamen.extend(["Jonas", "Dioan"])
schuelernamen.insert(1, "Manfred")
schuelernamen.pop(2)
schuelernamen.remove("Jonas")
print(schuelernamen.index("Jan"))
print(schuelernamen)
# Aufgabe 2
zahlenliste = []
while (True):
    userinput = input("Eingabe: ")
    match(userinput):
        case "Einfügen":
            zahlenliste.append(int(input("Zahl? ")))
        case "Ausgben":
            print(zahlenliste)
        case "Länge":
            print(len(zahlenliste))
        case "LöscheZahlAnPosition":
            userpos = int(input("Position?"))
            if ((len(zahlenliste)-1) >= userpos):
                zahlenliste.pop(userpos)
            else:
                print("Fehler")
        case "LöscheAlleZahlen":
            zahlenliste = []
        case "Ende":
            break
