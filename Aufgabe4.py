# Aufgabe 4 - Die ersten n nicht-negativen ganzen Zahlen drucken
def drucke_ganze_zahlen(p):
    for i in range(0, p):
        print(i, end=" ")  # Druckt die Zahlen von 0 bis p-1

drucke_ganze_zahlen(10)  # Druckt die ersten 10 nicht-negativen ganzen Zahlen
print()  # Neue Zeile


def print_integers(p):
    # Implementiere die Funktion hier
    for i in range(0, p):
        print(i, end=" ")

# Beispielaufruf der Funktion mit Argument 10
print_integers(10)
print()  # Diese Zeile sorgt für eine neue Zeile nach der Ausgabe
