"""
2
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
"""

numbers_list = [1, 2, 4, 8, 3, 6, 5, 7, 6, 5, 1, 2, 8]


def not_repetition(numb_list):
    for item in numb_list:
        if numb_list.count(item) == 1:
            yield item


for el in not_repetition(numbers_list):
    print(el)
