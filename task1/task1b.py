for number in range(95632, 95701):
    even_divisors = []
    for candidate in range(1, number+1):
        if number % candidate == 0:
            if candidate%2 == 0:
                even_divisors.append(candidate)        
    if len(even_divisors) == 6:
        print(*even_divisors, sep="\t")