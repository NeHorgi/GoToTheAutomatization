"""
Задания:
Напишите функцию get_sum(value), принимающую любое значение, и возвращающую
сумму его чисел, если это возможно, и None ,если невозможно.
Пример:
get_sum(123)
6
(т.е. 1+2+3)
"""

from typing import Any


def get_sum(value) -> Any:

    result = 0

    if isinstance(value, int):
        while value > 0:
            digit = value % 10
            result += digit
            value = value // 10
        return result

    if isinstance(value, float):
        value = str(value)
        value = value.replace('.', '')
        value = list(value)
        value = map(int, value)
        result = sum(value)
        return result

    if isinstance(value, bool):
        return None

    if value is None:
        return None

    for num in value:
        try:
            result += int(num)
        except ValueError:
            continue

    if abs(result) >= 0:
        return result
    else:
        return None


'''
<--------------------------------------------------------------------------------------------------------------------->
'''


"""
3. Есть функция:
"""


def add_gold(value):
    if value > 2_000:
        raise RuntimeError('Cannot add so much:( Please mercy!')
    print(f'{value} of gold added:) I am breathtaking!')


"""
Невозможно начислить больше 1000 золота за раз.
Напишите функцию add_some_gold(value), принимающую любое значение, и начислите 
требуемое количество золота используя функцию add_gold.
"""


def add_some_gold(value):
    div, mod = divmod(value, 1000)
    [add_gold(1000) for _ in range(div)]
    add_gold(mod)


'''
<--------------------------------------------------------------------------------------------------------------------->
'''

'''
Ниже представлена функция, которая выполняет поставленную выше задачу, но, когда нам не известно предельное значение, 
которое может быть обработано функцией add_gold().
'''


def add_some_gold_new(value):
    check_gold = value
    need_gold = value

    while True:
        try:
            add_gold(check_gold)
            break
        except RuntimeError:
            check_gold = check_gold / 2

    print(f'Функция начисления золота выполняет свою работу при значении {check_gold}')
    print()

    while need_gold > 0:
        add_gold(check_gold)
        need_gold -= check_gold


if __name__ == '__main__':
    '''
    print(get_sum(123))
    print(get_sum(None))
    print(get_sum([1, -1]))
    print(get_sum([-1, -1]))
    print(get_sum(2.124))
    print(get_sum('123'))
    print(get_sum('abs124fds'))
    print(get_sum([1, 2, 3]))
    print(get_sum({1, 2, 'f', 4}))
    '''
    add_some_gold_new(10000)
