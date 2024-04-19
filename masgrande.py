
def guess_number_iterative(n, x):
    contador = 0
    a = 0
    m = 0
    while m != x:
        if (n + a) % 2 == 0:
            m = (n + a) // 2
        else:
            m = (n + a) // 2 + 1
        
        if x > m:
            a = m 
        elif m > x:
            n = m
        
        contador += 1
    
    print(f'El numero es {m} y tomó {contador} repeticiones encontrarlo.')
    return m, contador

def guess_number(n, x, low=1, high=None, attempt=1):
    if high is None:
        high = n
    
    # Calculate mid point
    mid = (low + high) // 2
    
    # Base case: number found
    if mid == x:
        print(f'El numero es {mid} y tomó {attempt} repeticiones encontrarlo.')
        return mid
    
    # Base case: number not in range
    if low > high:
        print("Number not found.")
        return None
    
    # Recursive cases
    if x < mid:
        return guess_number(n, x, low, mid - 1, attempt + 1)
    else:
        return guess_number(n, x, mid + 1, high, attempt + 1)


def main():
    n = int(input("Introduzca el valor de n: "))
    x = float(input("Introduzca el numero a adivinar: "))
    
    print("\nIterative Approach:")
    guess_number_iterative(n, x)
    
    print("\nRecursive Approach:")
    guess_number(n, x)

if __name__ == "__main__":
    main()


