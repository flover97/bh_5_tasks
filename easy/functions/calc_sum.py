"""
Написать функцию calc_sum, которая принимает неограниченное количество целых
чисел и  возвращает их сумму

для расчета суммы можно воспользоваться функцией sum
"""


def calc_sum(*nums: int):
    result = sum(nums)
    return result


if __name__ == '__main__':
    print(calc_sum(1, 2, 3, 4))