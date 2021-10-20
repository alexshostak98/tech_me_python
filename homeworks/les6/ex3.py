"""
3
На вход функции подается строка, вернуть булевое является эта строка полиндромом или нет
проверочная строка "Пал, а норов худ и дух ворона лап."
Полиндром это строка которая читается в обе стороны одинаково, при этом знаки препинания числа и непечатные символы
игнорируются
"""

input_palindrome = "Пал, а норов худ и дух ворона лап."


def is_alpha(string):
    new_string = ''
    for item in string.lower():
        if item.isalpha():
            new_string += item
    return new_string


def check_palindrome(func, string):
    result = True
    return result if func(string) == func(string[::-1]) else not result


print(check_palindrome(is_alpha, input_palindrome))
