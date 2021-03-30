"""
Написать функцию to_set, которая принимает список, а возвращает множество,
созданное из этого списка и длину этого множества
"""


some_list = [1, 2, 3, 4]


def to_set(some_list: list):
    some_set = set(some_list)
    result = len(some_set)
    return some_set, result


if __name__ == '__main__':
    print(to_set(some_list))