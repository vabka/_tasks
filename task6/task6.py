# по аналогии с заданием 5 наше число должно иметь вид (2^n)*p^4 - у него будут нечётные делители 1, p, p^2, p^3, p^4

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, math.floor(math.sqrt(n))+1, 2):
        if n % i==0: return False
    return True

for i in range(35_000_000, 40_000_001):
    n = i
    while n%2 == 0: n //= 2 # спускаемся до возможного p^4 
    q = int(n**0.25) # возможный p
    if n == q**4 and is_prime(q):
        print(i)


