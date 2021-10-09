"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
"""

error = True
while error:
    input_number = input(
        "Input a number of month from 1 to 12\n>>"
    )
    if not input_number.isdigit():
        print("Input error")
    elif 0 < int(input_number) < 13:
        input_number = int(input_number)
        season = 'Spring' * (2 < input_number < 5) + \
                 'Summer' * (5 < input_number < 9) + \
                 'Autumn' * (8 < input_number < 12) \
                 or 'Winter'
        print(season)
        error = not error
    else:
        print("Input error")
