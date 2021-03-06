"""
2.1
Дан словарь с кодированием строк азбуки Морзе
Реализовать функцию кодирующую текст в морзе строку на вход которой подается строка текста, в ответ возвращается
строка закодированная азбукой морзе. В качестве разделителя морзе символов использовать пробел.
Пробел кодируется тоже как пробел.
Обратите внимание что используется только символы латинского Алфавита в lower case.
При этом строка должна всегда начинаться с заглавной буквы
"""

MORSE = {'.-': 'a', '-...': 'b', '-.-.': 'c',
         '-..': 'd', '.': 'e', '..-.': 'f',
         '--.': 'g', '....': 'h', '..': 'i',
         '.---': 'j', '-.-': 'k', '.-..': 'l',
         '--': 'm', '-.': 'n', '---': 'o',
         '.--.': 'p', '--.-': 'q', '.-.': 'r',
         '...': 's', '-': 't', '..-': 'u',
         '...-': 'v', '.--': 'w', '-..-': 'x',
         '-.--': 'y', '--..': 'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
         }

input_text = 'Hello mister Jingles'


def morse_code(text, morse_dict):
    """
    Return the text string was encrypted by Morse code
    """
    coded_text = ''
    morse = dict(zip(morse_dict.values(), morse_dict.keys()))
    for item in text.lower():
        if item == ' ':
            coded_text += item
            continue
        coded_text += item.replace(item, f'{morse[item]} ')
    return coded_text


print(morse_code(input_text, MORSE))
