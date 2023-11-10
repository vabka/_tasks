def get_natural_divisors(number: int) -> list[int]:
    """
    Получить список из натуральных делителей числа, отсортированных по возрастанию
    """
    result = []
    for candidate in range(1, number+1):
        if number % candidate == 0:
            result.append(candidate)
    return result

def filter_even(numbers: list[int]) -> list[int]:
    """
    Отфильтровать из списка целых чисел только чётные. Порядок следования чисел сохраняется
    """
    result = []
    for i in numbers:
        if i % 2 == 0:
            result.append(i)
    return result


# [95632; 95701]
for number in range(95632, 95701):
    divisors = get_natural_divisors(number)
    even_divisors = filter_even(divisors)    
    if len(even_divisors) == 6:
        print(*even_divisors, sep="\t")