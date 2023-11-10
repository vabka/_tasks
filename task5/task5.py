# 1. Число должно быть чётным
# 2. Если у числа есть как минимум два простых нечётных делителя (2pq, где p и q - простые), то у числа будет как минимум 4 чётных делителя 2, 2p, 2q, 2pq
# 3. Если число имеет форму 2p (где p - простое), то тогда у него будет только два чётных делителя: 2, 2p
# 4. Приходим к выводу, что наше число должно иметь форму 2p^2 где p - простое

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

def lp(n):
    p = int(math.floor(math.sqrt(n//2)))
    return p+1 if p%2 == 0 else p

a = lp(106_000_000) # Нижняя граница поиска простых чисел
b = lp(107_000_000) # Верхняя граница поиска простых чисел
for i in range(a, b):
    if is_prime(i):
        print(2*i*i)