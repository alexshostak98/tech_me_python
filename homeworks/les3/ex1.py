"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

пример списка: [22, 11, 45, 87, 0, 1, 6]
результат работы алгоритма с данным списком: [11, 22, 87, 45, 1, 0, 6]

будьте внимательны, пользователь необзательно в качестве значений введет числа, преобразованием и проверками
заниматься не надо, только разделить то что ввел пользователь и получить список значений.
"""

value_list = input(
    "Input some space separated values\n>>"
).split()
index = 0
last_index = len(value_list) - 1
while index < last_index:
    value_list[index], value_list[index + 1] = value_list[index + 1], value_list[index]
    index += 2
print(value_list)
