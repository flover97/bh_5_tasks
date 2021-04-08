"""
Написать рекурсивную функцию, которая будет вычислять сумму цифр целого числа

Можно пользоваться только функциями, операторами и условиями
"""


def calc_sum(n: int):
    if n <= 1:
        return n
    else:
        return n + calc_sum(n - 1)


if __name__ == '__main__':
    summ = calc_sum(10)
    print(summ)
