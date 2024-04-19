def guess_number_iterative(n, x):
    low = 1
    high = n
    contador = 0

    while low <= high:
        mid = (low + high) // 2

        if mid == x:
            print(f'El número es {mid} y tomó {contador} repeticiones encontrarlo.')
            return mid
        elif mid < x:
            low = mid + 1
        else:
            high = mid - 1

        contador += 1

    print("Número no encontrado.")
    return None

def guess_number_recursive(n, x, low=1, high=None, contador=0):
    if high is None:
        high = n

    if low > high:
        print("Número no encontrado.")
        return None

    mid = (low + high) // 2

    if mid == x:
        print(f'El número es {mid} y tomó {contador} repeticiones encontrarlo.')
        return mid
    elif x < mid:
        return guess_number_recursive(n, x, low, mid - 1, contador + 1)
    else:
        return guess_number_recursive(n, x, mid + 1, high, contador + 1)

def main():
    n = int(input("Introduce el valor de n: "))
    x = int(input("Introduce el número a adivinar: "))

    print("\nMétodo Iterativo:")
    guess_number_iterative(n, x)

    print("\nMétodo Recursivo:")
    guess_number_recursive(n, x)

if __name__ == "__main__":
    main()
