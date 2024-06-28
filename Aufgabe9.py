import random
import string


def generiere_passwort(laenge):
    # Definiere einen Pool von Zeichen, aus denen das Passwort generiert werden soll
    zeichen_pool = string.ascii_letters + string.digits + string.punctuation

    # Initialisiere eine leere Zeichenkette, um das Passwort zu speichern
    passwort = ''

    # Schleife über die gewünschte Länge des Passworts, um zufällige Zeichen hinzuzufügen
    for _ in range(laenge):
        # Wähle zufällig ein Zeichen aus dem Pool aus und füge es dem Passwort hinzu
        passwort += random.choice(zeichen_pool)

    # Gebe das generierte Passwort zurück
    return passwort


# Testbeispiele
print(generiere_passwort(12))  # Beispiel für ein Passwort der Länge 12
print(generiere_passwort(8))  # Beispiel für ein Passwort der Länge 8
print(generiere_passwort(16))  # Beispiel für ein Passwort der Länge 16
