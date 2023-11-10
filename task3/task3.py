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

for number in range(120115, 120201):
    divisors = get_natural_divisors(number)
    # Так как мы перебираем числа от меньшего к большему,
    #  то следующее число гарантированно будет больше предыдущего,
    #  что как раз необходимо нам по условию (если у двух чисел одинаковое количество делителей, то вывести надо большее их них)
    if len(divisors) >= max_divisors:
        max_divisors = len(divisors)
        max_number = number

print(max_divisors, max_number)