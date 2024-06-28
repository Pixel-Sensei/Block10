# Aufgabe 6 - Summe aller Ziffern
def summe_der_ziffern(number):
    if number == 0:
        return 0  # Basisfall: Wenn die Zahl 0 ist, ist die Summe der Ziffern 0
    else:
        return number % 10 + summe_der_ziffern(int(number / 10))  # Rekursive Berechnung der Summe der Ziffern

meine_zahl = 2345341239
print("Die Summe der Ziffern in", meine_zahl, "ist", summe_der_ziffern(meine_zahl))  # Ausgabe der Summe der Ziffern
