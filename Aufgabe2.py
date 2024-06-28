# Aufgabe 2 - Zweitkleinsten Wert löschen
meineListe = [10, 2, 5, 4, 42, 1]

def loesche_zweitkleinsten(p):
    p = sorted(p)  # Sortiert die Liste
    p.remove(p[1])  # Entfernt den zweitkleinsten Wert (an Index 1)
    return p  # Gibt die modifizierte Liste zurück

meineListe = loesche_zweitkleinsten(meineListe)  # Aktualisiert die Liste mit der modifizierten Liste
print(meineListe)  # Gibt die modifizierte Liste aus