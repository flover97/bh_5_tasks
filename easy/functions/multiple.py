"""
Написать функцию multiply, которая принимает аргумент n.
и возвращает функцию closure, которая принимает аргумент x и возвращает x * n
"""


def multiply(n: int):
    def closure(x: int):
        result = x * n
        return result
    return closure


if __name__ == '__main__':
    n_num = multiply(2)
    x_num = n_num(5)
    print(x_num)
