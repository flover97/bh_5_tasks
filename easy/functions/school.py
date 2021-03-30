"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция decr_students, которая принимает SCHOOL_DATA, название класса и
    уменьшает количество учеников на 1, но не меньше 0
- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
- Функция remove_class, которая принимает SCHOOL_DATA, название класса и удаляет
    класс из словаря
- Функция calc_students, которая принимает SCHOOL_DATA и возвращает кол-во
    учеников во всей школе
"""
SCHOOL_DATA = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}


def inc_students(school_cls: dict, n_class: str):
    school_cls[n_class] += 1
    return school_cls


def derc_student(school_cls: dict, n_class: str):
    if school_cls[n_class] > 0:
        school_cls[n_class] -= 1
        return school_cls


def add_class(school_cls: dict, n_class: str):
    new_cls = {n_class: 0}
    school_cls.update(new_cls)
    return school_cls


def remove_class(school_cls: dict, n_class: str):
    school_cls.pop(n_class)
    return school_cls


def calc_students(school_cls: dict):
    stud_sum = sum(school_cls.values())
    return stud_sum


if __name__ == '__main__':
    print(inc_students(SCHOOL_DATA, "1a"))
    print(derc_student(SCHOOL_DATA, "1a"))
    print(add_class(SCHOOL_DATA, "3a"))
    print(remove_class(SCHOOL_DATA, "3a"))
    print(calc_students(SCHOOL_DATA))
