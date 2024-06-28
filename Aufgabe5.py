# Aufgabe 5 - Summe der Matrixelemente
# Lösung 1
def matrix_summe(data):
    total = 0
    for row in data:
        for item in row:
            total += item  # Fügt jedes Element zur Gesamtsumme hinzu
    return total  # Gibt die Gesamtsumme zurück

print("Die Summe aller Werte:", matrix_summe([[1, 2], [3, 4], [5, 6], [7, 8]]))  # Ausgabe der Summe

# Lösung 2
def rekursive_matrix_summe(data):
    total = 0
    for element in data:
        if isinstance(element, list):  # Überprüft, ob das Element eine Liste ist
            total = total + rekursive_matrix_summe(element)  # Rekursive Aufruf für die Liste
        else:
            total = total + element  # Fügt das Element zur Gesamtsumme hinzu
    return total  # Gibt die Gesamtsumme zurück

print("Die Summe aller Werte:", rekursive_matrix_summe([[1, 2], [3, 4], [5, 6], [7, 8]]))  # Ausgabe der Summe
