def get_natural_divisors(number: int) -> list[int]:
    """
    Получить список из натуральных делителей числа, отсортированных по возрастанию
    """
    result = []
    for candidate in range(1, number+1):
        if number % candidate == 0:
            result.append(candidate)
    return result

# У любого числа всегда будет как минимум один делитель
max_divisors=0
max_number=None

for number in range(84052, 84131):
    divisors = get_natural_divisors(number)    
    # Так как мы перебираем числа от меньшего к большему,
    # следующее число гарантированно больше, чем любое предыдущее.
    # Так как мы ищем наименьшее число с наибольшим количеством делителей,
    # мы переходим к большему числу только тогда, когда у него делителей больше, чем у всех предыдущих
    if len(divisors) > max_divisors:
        max_divisors = len(divisors)
        max_number = number

print(max_divisors, max_number)