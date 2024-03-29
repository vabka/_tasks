# Декомпозиция

> Декомпозиция — операция мышления, состоящая в разделении целого на части.\
Также декомпозицией называется общий приём, применяемый при решении проблем, состоящий в разделении проблемы на множество частных проблем, а также задач, не превосходящих суммарно по сложности исходную проблему, с помощью объединения решений которых, можно сформировать решение исходной проблемы в целом.

Декомпозиция - это очень важный навык, который пригодится не только лишь в программировании, но и в любом другом деле, в том числе в учёбе или работе в будущем.

Пример декомпозиции задачи на примере известной шутки:
> Как засунуть слона в холодильник?
>
> 1. Открыть холодильник
> 2. Засунуть положить в холодильник
> 3. Закрыть холодильник
>
> Как засунуть жирафа в холодильник?
> 1. Открыть холодильник
> 2. Вытащить слона
> 3. Положить в холодильник
> 4. Закрыть холодильник

Но декомпозировать можно не только задачи, но и вообще любой объект или определение.
Например:
> Автомобиль:
> - Механический (приводится в движение двигателем, а мускульной силой человека или лошади)
> - Транспортное средство (устройство, предназначенное для перемещения людей или грузов)
> - Имеет не менее четырёх колёс (не два и не гусеницы)
> - Имеет как минимум две оси
> - Не трактор
> - Не квадрицикл
> - Не самоходная машина
>
> (ПДД, определение транспортного средства)


В программировании часто бывают ситуации, когда для получения решения (программы), достаточно 1-в-1 перевести условия задачи в код, но чтобы это сделать, нужно сначала задачу разделить на несколько простых и однозначных шагов (декомпозировать).

Пример:
> Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [95632; 95700], числа, имеющие ровно шесть различных чётных натуральных делителей (при этом количество нечётных делителей может быть любым). Для каждого найденного числа запишите эти шесть делителей в шесть соседних столбцов на экране с новой строки.

Задача большая, но после декомпозиции выглядит сильно лаконичнее:

Программа должна:
1. Взять числа на отрезке [95632; 95700]
2. Для каждого из этих чисел найти уникальные натуральные делители.
3. Посчитать, сколько из этих делителей чётные
4. Взять только те числа, у которых чётных делителей ровно 6
5. Для каждого из оставшихся чисел, вывести список из этих делителей


В качестве домашнего задания
1. Проведи подобную декомпозицию для заданий 2,3,4,5,6.
2. Приведи три примера декомпозиции из жизни. (Например, это может быть процесс уборки, готовки еды, сбора вещей в поездку или в школу, или даже правила/игровой процесс какой-нибудь видеоигры).
