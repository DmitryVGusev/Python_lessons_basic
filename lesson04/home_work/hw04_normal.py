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


# print(parse_line1(line))
# print(parse_line1_re(line))

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
    pattern = '[a-z]{2}([A-Z]+)[A-Z]{2}'
    return re.findall(pattern, line)


def parse_line2(line):

    def char_is_up(char):
        if ord(char) in range(ord('A'), ord('Z') + 1):
            return True
        else:
            return False


    def left(line, i):
        if ord(line[i-1]) in range(ord('a'), ord('z') + 1) and ord(line[i-2]) in  range(ord('a'), ord('z') + 1):
            return True
        else:
            return False

    def right(line, i):
        if ord(line[i+1]) in range(ord('A'), ord('Z') + 1) and ord(line[i+2]) in range(ord('A'), ord('Z') + 1):
            return True
        else:
            return False

    el = ''
    result = []
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
