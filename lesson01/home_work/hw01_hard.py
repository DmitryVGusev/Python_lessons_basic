# -*- coding: utf-8 -*-

__author__ = 'Гусев Дмитрий Вадимович'

# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True

# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось?

# Подсказка: это значение точно есть ;)
"""
Изначально, хотел ответить что какой-то объект, магические методы которого переопределены.
Но оказалось проще. Хотя, недалеко ушел от истины.
"""
a = float('inf')
