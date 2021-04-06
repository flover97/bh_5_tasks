"""
Написать генератор triangular_numbers, который возвращает подряд числа
треугольные числа


Формула:

Tn = 1 / 2 * n * (n + 1)


Например:

tn_gen = triangular_numbers()

next(tn_gen) -> 1
next(tn_gen) -> 2
next(tn_gen) -> 6
next(tn_gen) -> 24
"""


def triangular_numbers(n):
    for i in range(1, n + 1):
        tn = 1 / 2 * i * (i + 1)
        yield tn


if __name__ == '__main__':
    tn_gen = triangular_numbers(20)
    print(next(tn_gen))
    print(next(tn_gen))
    print(next(tn_gen))
    print(next(tn_gen))
    print(next(tn_gen))
    print(next(tn_gen))

