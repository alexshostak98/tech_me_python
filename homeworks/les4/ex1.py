import random
"""
Даны матрицы n на m
Матрица олицетворяет улицу, колонки в Матрице олицетворяют Здания. 1 в колонке означает наличие этажа, 0 его отсутвие
Написать алгоритм нахождения самого высокого здания на улице. результат сохранить в переменную в виде кортежа или
списка [номер колонки, количество этажей]
"""
"""
пример матрицы:
some_builds = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 1, 0],
    [1, 1, 1, 1]
]
результат для данной матрицы = [3, 4] 3 - колонка, 4 - высота здания
"""

buildings = input("Введите число зданий на улице\n>>")
floors = input("Введите максимальное количество этажей здания\n>>")
has_floor = 1
hasnt_floor = 0
if buildings.isdigit() and floors.isdigit():
    buildings = int(buildings)
    floors = int(floors)
    matrix_1 = []
    for item_1 in range(floors):
        row = []
        for item_2 in range(buildings):
            row.append(random.randint(hasnt_floor, has_floor))
        matrix_1.append(row)
    print(f'Исходная матрица: {matrix_1}')
else:
    print("Ошибка ввода. Только целые положительные числа")
matrix_2 = []
for items in zip(*matrix_1):
    matrix_2.append(sum(items))
building_height = max(matrix_2)
building_number = matrix_2.index(building_height) + 1
result = [building_number, building_height]
print(f'Результат работы: {result}')
