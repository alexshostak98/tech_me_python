"""
Дано 2 Матрицы
Необходимо получить произведение данных матриц
"""
row_count_1 = input("Введите количество строк матрицы А\n>>")
error = "Ошибка ввода. Только числа"
matrix_1 = []
if row_count_1.isdigit():
    for val_1 in range(int(row_count_1)):
        input_row_1 = input("Заполните строку матрицы А\n>>").split(" ")
        row_1 = []
        for val_2 in input_row_1:
            if val_2.isdigit():
                val_2 = int(val_2)
                row_1.append(val_2)
        matrix_1.append(row_1)
else:
    print(error)
row_count_2 = input("Введите количество строк матрицы В\n>>")
matrix_2 = []
if row_count_2.isdigit():
    for val_3 in range(int(row_count_2)):
        input_row_2 = input("Заполните строку матрицы В\n>>").split(" ")
        row_2 = []
        for val_4 in input_row_2:
            if val_4.isdigit():
                val_4 = int(val_4)
                row_2.append(val_4)
        matrix_2.append(row_2)
else:
    print(error)
print(f'Матрица А: {matrix_1}\nМатрица В: {matrix_2}')

if len(matrix_1[0]) == len(matrix_2):
    matrix_2_rotate = []
    for rows_1 in zip(*matrix_2):
        matrix_2_rotate.append(rows_1)
    matrix_3 = []
    n = 0
    while n < len(matrix_2_rotate):
        column = []
        for item_1 in matrix_1:
            rows = []
            for element_1, element_2 in zip(item_1, matrix_2_rotate[n]):
                rows.append(element_1 * element_2)
            column.append(sum(rows))
        matrix_3.append(column)
        n += 1
    final_matrix = []
    for rows_2 in zip(*matrix_3):
        final_matrix.append(rows_2)
    print(f'Матрица АВ: {final_matrix}')
else:
    print("Выполнить умножение данных матриц невозможно")
