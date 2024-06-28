# Aufgabe 1 - Probe
def keine_parameter():
    return [2, 5]  # Gibt eine Liste mit den Zahlen 2 und 5 zurück

def mit_parameter(p, q):
    return p * q  # Multipliziert die beiden Parameter und gibt das Ergebnis zurück

keine_parameter()  # Ruft die Funktion ohne Parameter auf
mit_parameter(2, 3)  # Ruft die Funktion mit den Parametern 2 und 3 auf
mit_parameter(q=3, p=2)  # Ruft die Funktion mit benannten Parametern auf
mit_parameter(2, q=3)  # Ruft die Funktion mit einem benannten und einem unbenannten Parameter auf
