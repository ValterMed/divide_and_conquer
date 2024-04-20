def adivinar_numero_iterativo(n, x):
    intentos = 0
    inicio = 1
    fin = n
    while inicio <= fin:
        intentos += 1
        medio = (inicio + fin) // 2
        if medio == x:
            return intentos
        elif medio < x:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

n = 100  # El rango de números
x = 39  # El número a adivinar
print(adivinar_numero_iterativo(n, x))
