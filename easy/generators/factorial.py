"""
Написать генератор factorial, который возвращает подряд числа факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""


def factorial(x):
    a = 1
    for i in range(1, x+1):
        a *= i
        yield a


if __name__ == '__main__':
    factorial_gen = factorial(10)
    print(next(factorial_gen))
    print(next(factorial_gen))
    print(next(factorial_gen))
    print(next(factorial_gen))
    print(next(factorial_gen))
