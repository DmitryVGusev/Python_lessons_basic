# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

import re

"""
Мне пример кажется некорректным.
- из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
Нулевой элемент ('mt') не имеет слева 1 или более символов в верхнем регистре.
Тем не мение, в ответе он присутствует.
На основе этого будем считать что начало строки и конец строки считаются.
Также, для упрощения будем считать что строка содержит только символы [a-z] и [A-Z].
"""

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

def parse_line1_re(line):
    """
    Выводит символы в нижнем регистре, которые находятся вокруг 1
        или более символов в верхнем регистре, используя регулярные выражения.
    :param line: Строка для обработки
    :return: Список с обработанными элементами
    """
    pattern = '[A-Z]*([a-z]+)[A-Z]*'
    return re.findall(pattern, line)


def parse_line1(line):
    """
    Выводит символы в нижнем регистре, которые находятся вокруг 1
        или более символов в верхнем регистре, без использования регулярных выражений.
    :param line: Строка для обработки
    :return: Список с обработанными элементами
    """

    # Инициализируем переменные
    i = 0
    result = []
    el = ''  # Элемент в списке результата

    # Проходимся посимвольно по строке
    for i in line:
        # Если встречаем букву в верхнем регистре - добавляем элемент в список результата
        if ord(i) in range(ord("A"), ord("Z") + 1):
            if el:
                result.append(el)
                el = ''
        # Если встречаем букву в нижнем регистре - добавляем к элементу
        else:
            el += i

    # Добавляем элемент в список результатов
    if el:
        result.append(el)

    return result


# Вывод результатов
print(parse_line1(line))
print(parse_line1_re(line))

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'


def parse_line2_re(line):
    """
    Выводит символы в верхнем регистре, слева от которых находятся два символа в нижнем регистре,
      а справа - два символа в верхнем регистре. Реализуется с помощью регулярных переменных.
    :param line: строка с символами
    :return: список последовательностей
    """
    pattern = '[a-z]{2}([A-Z]+)[A-Z]{2}'
    return re.findall(pattern, line)


def parse_line2(line):
    """
    Выводит символы в верхнем регистре, слева от которых находятся два символа в нижнем регистре,
      а справа - два символа в верхнем регистре.
    :param line: строка с символами
    :return: список последовательностей
     """

    def char_is_up(char):
        """Проверяет если выбранный символ является заглавной буквой"""
        if ord(char) in range(ord('A'), ord('Z') + 1):
            return True
        else:
            return False


    def left(line, i):
        """Проверяет если слева от выбранного элемента два символа в нижнем регистре"""
        if ord(line[i-1]) in range(ord('a'), ord('z') + 1) and ord(line[i-2]) in  range(ord('a'), ord('z') + 1):
            return True
        else:
            return False

    def right(line, i):
        """Проверяет если справа от выбранного элемента два символа в верхнем регистре"""
        if ord(line[i+1]) in range(ord('A'), ord('Z') + 1) and ord(line[i+2]) in range(ord('A'), ord('Z') + 1):
            return True
        else:
            return False

    el = ''
    result = []
    # Проверка что с левой стороны выбранного элемента два символа в нижнем регистре"
    is_left_part_present = False


    for i in range(2, len(line)-2):
        if char_is_up(line[i]):
            if is_left_part_present or left(line, i):
                if right(line, i):
                    el += line[i]
                    is_left_part_present = True
                else:
                    if el:
                        result.append(el)
                        el = ''
                        is_left_part_present = False
        else:
            continue
    return result


# Вывод результатов
print(parse_line2_re(line_2))
print(parse_line2(line_2))

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
from random import randint
from itertools import groupby


def fill_file(filename: str):
    """
    Заполняет указанный файл произвольными целыми цифрами,
    в результате в файле должно быть 2500-значное произвольное число
    :param filename: путь/имя_файла
    :return: None
    """

    # Создаем список из 2500 произвольных чисел от 0 до 9
    number = [str(randint(0, 9)) for _ in range(2500)]

    # Записываем список в файл, предварительно переведя его в строку
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(''.join(number))


def count_max_same_number_length(filename: str):
    """
    Находит самую длинную последовательность одинаковых цифр в числе в заданном файле
    :param filename: имя файла
    :return: Список с самой длинной последовотельностью одинаковых чисел
    """

    # Считываем строку из файла
    with open(filename, 'r', encoding='utf-8') as f:
        number = f.readline().strip()

    # Группируем строки по последовательности одинаковых цифр
    grouped = [list(g) for k, g in groupby(number)]

    # Возвращаем максимально длинную последовательность
    return max(grouped, key=len)


# Проверка результатов
fill_file('some.txt')
print(count_max_same_number_length('some.txt'))
