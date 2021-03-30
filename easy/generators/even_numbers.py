"""
Написать генератор get_even_number, который возвращает подряд четные числа

Например:

even_gen = get_even_number()

next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""


def get_even_number(n: int):
    for x in range(n):
        if x != 0:
            if x % 2 == 0:
                yield x


if __name__ == '__main__':
    even_gen = get_even_number(100)
    print(next(even_gen))
    print(next(even_gen))
    print(next(even_gen))
    print(next(even_gen))