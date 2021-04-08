"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и 
False, если нет

Нельзя пользоваться операцией возведения в степень
"""


def is_power(n):
    if n == 2:
        return True
    elif n % 2 != 0:
        return False
    else:
        return is_power(n / 2.0)


if __name__ == '__main__':
    print(is_power(6))
