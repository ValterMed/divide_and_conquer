def adivinar_numero_recursivo(inicio, fin, x, intentos=0):
    if inicio > fin:
        return -1
    intentos += 1
    medio = (inicio + fin) // 2
    if medio == x:
        return intentos
    elif medio < x:
        return adivinar_numero_recursivo(medio + 1, fin, x, intentos)
    else:
        return adivinar_numero_recursivo(inicio, medio - 1, x, intentos)

inicio = 1  # El inicio del rango
fin = 100  # El fin del rango
x = 39  # El número a adivinar
print(adivinar_numero_recursivo(inicio, fin, x))