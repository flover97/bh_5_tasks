"""
Написать рекурсивную функцию  line_print, которая принимает 1 аргумент - список

Функция печатает каждых элемент на новой строке.

Если элемент списка - список, то его элементы должны выводиться с отступом
относительно родительского на одну табуляцию

Например:

some_list = [1, 2, [1, 2, [5, 7], 3], 8]

line_print(some_list)
1
2
    1
    2
        5
        7
    3
8
"""
some_list = [1, 2, [1, 2, [5, 7], 3], 8]


def rec_increment(lst, depth=0):
    for element in lst:
        if isinstance(element, list):
            depth += 1
            rec_increment(element, depth)
        else:
            print("\t " * depth + str(element))


if __name__ == '__main__':
    rec_increment(some_list)