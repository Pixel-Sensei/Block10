# Aufgabe 8 - Einzigartiger Charakter im String
def einzigartiger_charakter(string):
    string = string.lower()  # Konvertiert den String in Kleinbuchstaben
    haeufigkeit = {}
    for i in string:
        if i not in haeufigkeit:
            haeufigkeit[i] = 1  # Initialisiert die Häufigkeit des Charakters
        else:
            haeufigkeit[i] += 1  # Erhöht die Häufigkeit des Charakters
    for i in range(len(string)):
        if haeufigkeit[string[i]] == 1:  # Findet den ersten einzigartigen Charakter
            return i  # Gibt den Index des einzigartigen Charakters zurück
    return -1  # Gibt -1 zurück, wenn kein einzigartiger Charakter gefunden wurde

print(einzigartiger_charakter("Wohin du auch gehst, egal wie das Wetter ist, bring immer deinen eigenen Sonnenschein mit."))  # Ausgabe des Index des ersten einzigartigen Charakters


