def zaehle_kleinbuchstaben(satz):
    """
    Diese Funktion zählt die Anzahl der Kleinbuchstaben in einem gegebenen Satz.

    Args:
    - satz (str): Der Eingabesatz, in dem die Kleinbuchstaben gezählt werden sollen.

    Returns:
    - int: Die Anzahl der Kleinbuchstaben im Satz.
    """
    anzahl_kleinbuchstaben = 0  # Initialisierung der Zählvariable für Kleinbuchstaben
    for buchstabe in satz:  # Iteriere über jeden Buchstaben im Satz
        if buchstabe.islower():  # Überprüfe, ob der Buchstabe ein Kleinbuchstabe ist
            anzahl_kleinbuchstaben += 1  # Wenn ja, erhöhe die Zählvariable um 1
    return anzahl_kleinbuchstaben  # Gebe die Gesamtanzahl der Kleinbuchstaben zurück

# Beispielaufruf der Funktion und Ausgabe
satz = "Wohin du auch gehst, egal wie das Wetter ist, bring immer deinen eigenen Sonnenschein mit."
anzahl = zaehle_kleinbuchstaben(satz)  # Aufruf der Funktion, um die Anzahl der Kleinbuchstaben zu ermitteln
print("Anzahl der Kleinbuchstaben:", anzahl)  # Ausgabe der Anzahl der Kleinbuchstaben
