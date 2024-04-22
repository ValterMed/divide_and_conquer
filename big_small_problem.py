
def guessNumber(n, x):
    count = 0
    low, high = 1, n
    
    while low <= high:
        mid = (low + high) // 2
        count += 1
        
        if mid == x:
            return count
        elif mid < x:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

# Example
n = 100
x = 42
print("Número de intentos:", guessNumber(n, x))

# Recursive

def guessNumberRecursive(low, high, x, count):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    count += 1
    
    if mid == x:
        return count
    elif mid < x:
        return guessNumberRecursive(mid + 1, high, x, count)
    else:
        return guessNumberRecursive(low, mid - 1, x, count)

def guessNumber(n, x):
    return guessNumberRecursive(1, n, x, 0)

# Example
n = 100
x = 42
print("Número de intentos:", guessNumber(n, x))


