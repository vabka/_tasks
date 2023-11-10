def get_natural_divisors(number: int) -> list[int]:
    """
    Получить список из натуральных делителей числа, отсортированных по возрастанию
    """
    result = []
    for candidate in range(1, number+1):
        if number % candidate == 0:
            result.append(candidate)
    return result

# [201455; 201470]
for number in range(201455, 201471):
    divisors = get_natural_divisors(number)
    if len(divisors) == 4:
        print(*divisors, sep="\t")