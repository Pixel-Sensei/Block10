def bubble_sort(meineListe):
    n = len(meineListe)
    for i in range(n):
        for j in range(0, n-i-1):
            if meineListe[j] > meineListe[j+1]:
                meineListe[j], meineListe[j+1] = meineListe[j+1], meineListe[j]
    return meineListe

meineListe = [8, 3, 5, 1, 2, 7, 6, 9]
print("Bubble Sort:", bubble_sort(meineListe))
