"""
Написать рекурсивную функцию, которая будет вычислять сумму цифр целого числа

Можно пользоваться только функциями, операторами и условиями
"""


def calc_sum(*args):
    summa = 0
    for i in args:
        summa += i

    return sum(args)


if __name__ == '__main__':
    some_values = []
    while True:
        value = input('Введите число: ')
        if value == 'stop':
            break
        some_values.append(int(value))
    print(calc_sum(*some_values))