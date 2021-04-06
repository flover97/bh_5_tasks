"""
Написать рекурсивную функцию factorial, которая будет возвращать n-ый элемент
"""


def factorial(n, fct=1):
    for i in range(2, n + 1):
        fct *= i
    return fct


if __name__ == '__main__':
    print(factorial(4))
