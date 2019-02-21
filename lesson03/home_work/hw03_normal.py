# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
"""
Предположим, что при обращении к ряду Фибоначчи, счет начинают все же с первого элемента, а не с нулевого
"""


def fibonacci(n: int, m: int):
    """
    Функция, возращающая список из ряда Фибоначчи с n по m элемент
    :param n: первый элемент списка
    :param m: последний элемент списка
    :return: list
    """
    result = [1, 1]
    position = 2
    if n < 1:
        return None
    if n > m:
        return None
    while position < m:
        result.append(sum([result[-1], result[-2]]))
        position += 1
    return [result[x] for x in range(n-1, m)]


# Проверка результата
print(fibonacci(3, 6))  # return [2, 3, 5, 8]
print(fibonacci(0, 2))  # return None
print(fibonacci(-1, 20))  # return None
print(fibonacci(5, 4))  # return None
print(fibonacci(6, 6))  # return [8]

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
"""
Любой - так любой. Всегда мечтал реализовать рандомную сортировку =)
"""
from random import randint


def sort_to_max(origin_list:list):
    """
    Рандомная сортировка. Кажды раз меняет элементы местами до тех пор пока список не окажется отсортированным
    :param origin_list: список элементов
    :return: отсортированный список элементов
    """
    def is_sorted(l):
        """Проверяет отсортирован ли массив"""
        return all(l[i] <= l[i+1] for i in range(len(l)-1))

    result = origin_list
    iterations = 0  # Чисто удовольствия ради. Счетчик количества перетасовок

    # Бесконечный цикл пока итоговый список не окажется отсортирован
    while not is_sorted(result):
        iterations += 1

        # чтобы не испортить исходный список, создаем его копию
        elements_list = origin_list.copy()
        result = []
        while len(elements_list) > 0:
            # Вытаскиваем случайный элемент из списка и записываем в итоговый список
            result.append(elements_list.pop(randint(0, len(elements_list)-1)))

    print("Список отсортирован всего за {} попыток".format(iterations))

    return result

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def my_filter(func, lst: list):
    """
    Самописный метод реализации filter
    :param func: любая функция, возвращающая True или False
    :param lst: список
    :return: В отличие от классического filter, возвращает List а не filter object
    """
    result = []
    for i in lst:
        if func(i):
            result.append(i)
    return result


# Проверка результата
print(my_filter(lambda x: x > 0, [-1, 4, -4, 5]))  # return [4, 5]

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
from math import sqrt



# def is_parallelogram(A1: list, A2: list, A3: list, A4: list):
#     """Функция, возвращающая True если по четырем точкам можно построить параллелограм"""
#     # lambda - функция, реализующая теорему Пифагора о расстаянии между двумя точками
#     distance_between = lambda a, b: sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
#     triangle_sides = lambda a, b, c: [distance_between(a, b), distance_between(b, c), distance_between(a, c)]
#
#     if sorted(triangle_sides(A1, A2, A3)) != sorted(triangle_sides(A1, A4, A3)):
#         return False
#     elif sorted(triangle_sides(A1, A2, A4)) != sorted(triangle_sides(A4, A2, A3)):
#         return False
#     else:
#         return True
#
#
# medial_point = lambda a, b: [(b[0] + a[0])/2, (b[1] + a[1])/2]
#
# A1 = [0, 0]
# A2 = [6, 4]
# A3 = [5, 0]
# A4 = [1, 4]
#
# dots = [A1, A2, A3, A4]
# medials = []
# while len(dots) > 1:
#     dot = dots.pop(0)
#     for i in dots:
#         medials.append(medial_point(dot, i))
#
# print(medials)
#
# for point in dots:
#
#
#
#
# medials = [
#     medial_point(A1, A2),
#     medial_point(A1, A3),
#     medial_point(A1, A4),
#     medial_point(A2, A3),
#     medial_point(A2, A4),
#     medial_point(A3, A4)
# ]
# print(medials)


# def triangle_sides(a, b, c):
#     return [distance_between(a, b),
#             distance_between(b, c),
#             distance_between(a, c)]

