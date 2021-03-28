"""
Написать функцию bang, которая печатает "Boom"

Написать декоратор repeat_n_times, у которого есть параметр n.
Декоратор должен выполнить функцию bang n раз
"""

repeat = int(input("Кл-во повторений: "))


def repeat_n_times(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat_n_times(repeat)
def bang():
    print("Boom")


if __name__ == '__main__':
    bang()

