"""
3
Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg_1, arg_2, arg_3):
    """
    Return the sum of two bigger argument of the three
    """
    # if arg_1 < arg_2 and arg_1 < arg_3:
    if arg_2 > arg_1 < arg_3:
        return arg_2 + arg_3
    elif arg_2 < arg_3:
        return arg_1 + arg_3
    return arg_1 + arg_2


def my_func_1(arg_1, arg_2, arg_3):
    result = arg_1 + arg_2 + arg_3 - min(arg_1, arg_2, arg_3)
    return result


print(my_func(1, 3, 3))
print(my_func_1(1, 3, 3))
