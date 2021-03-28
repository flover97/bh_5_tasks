"""
Написать функцию get_even_number, которая принимает 1 аргумент - номер
четного числа и возвращает само четное число

Например:

- get_even_number(10) -> 20
- get_even_number(3) -> 6
"""


def get_even_number(num: int):
    if num != 0:
        print(num * 2)
    else:
        print("Число не четное")


if __name__ == '__main__':
    num_input = int(input("Введите номер четного числа: "))
    get_even_number(num_input)
