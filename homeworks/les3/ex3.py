"""
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

input_data = input(
    "Input string of words separated by space\n>>"
).split()
index = 0
list_length = len(input_data)
while index < list_length:
    string_number = index + 1
    print(f"{string_number}: {input_data[index][:10]:^10}")
    index += 1
