def sum_iterative(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result

# Beispielaufruf
n = 5
print(f"Die Summe der Zahlen von 1 bis {n} (iterativ): {sum_iterative(n)}")

def sum_recursive(n):
    if n == 1:
        return 1
    else:
        return n + sum_recursive(n - 1)

# Beispielaufruf
n = 5
print(f"Die Summe der Zahlen von 1 bis {n} (rekursiv): {sum_recursive(n)}")
