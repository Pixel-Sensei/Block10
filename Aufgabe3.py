# Aufgabe 3 - Ungerade Zahlen löschen
meineListe = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def loesche_ungerade(p):
    i = 0
    while i < len(p):
        if p[i] % 2 == 1:  # Prüft, ob die Zahl ungerade ist
            p.remove(p[i])  # Entfernt die ungerade Zahl
        else:
            i += 1  # Erhöht den Index, wenn die Zahl gerade ist
    return p  # Gibt die modifizierte Liste zurück

meineListe = loesche_ungerade(meineListe)  # Aktualisiert die Liste mit der modifizierten Liste
print(meineListe)  # Gibt die modifizierte Liste aus