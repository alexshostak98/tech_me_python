"""
1
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Результатом работы функции должна быть строка
Пример строки результата:
Иванов Иван Иванович 1986 года Рождения, проживающий в городе Норильск.
Контактные данные:
- телефон: 89181111111
- email: test@test.ru
"""

bio = ["Евгений", "Батиков", "1991", "Москва", "evgen_batikov@mail.ru", "+7123456789"]


def my_func(name, surname, birth_year, city, email, phone_number):
    """
    Return user data according to the template
    """
    result = f"{surname} {name} {birth_year} года рождения, проживающий в городе {city}.\nКонтактные данные:\n" \
             f"- телефон: {phone_number}\n- email: {email}"
    return result


print(my_func(*bio))
