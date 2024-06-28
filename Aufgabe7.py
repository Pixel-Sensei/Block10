# Aufgabe 7 - Mergesort
def merge_sort(meineListe):
    groesse = len(meineListe)
    if groesse > 1:
        mitte = groesse // 2  # Teilt die Liste in zwei Unterlisten
        linke_liste = meineListe[:mitte]
        rechte_liste = meineListe[mitte:]
        merge_sort(linke_liste)  # Rekursiver Aufruf für die linke Unterliste
        merge_sort(rechte_liste)  # Rekursiver Aufruf für die rechte Unterliste
        p = 0
        q = 0
        r = 0
        linke_groesse = len(linke_liste)
        rechte_groesse = len(rechte_liste)
        while p < linke_groesse and q < rechte_groesse:  # Mischen der Unterlisten
            if linke_liste[p] < rechte_liste[q]:
                meineListe[r] = linke_liste[p]
                p += 1
            else:
                meineListe[r] = rechte_liste[q]
                q += 1
            r += 1
        while p < linke_groesse:  # Fügt die restlichen Elemente der linken Liste hinzu
            meineListe[r] = linke_liste[p]
            p += 1
            r += 1
        while q < rechte_groesse:  # Fügt die restlichen Elemente der rechten Liste hinzu
            meineListe[r] = rechte_liste[q]
            q += 1
            r += 1
        return meineListe  # Gibt die sortierte Liste zurück

meineListe = [8, 3, 5, 1, 2, 7, 6, 9]
print()
print("Eingabearray:", meineListe, end="\n\n")
print()
print("Sortiertes Array:", merge_sort(meineListe))  # Ausgabe des sortierten Arrays
