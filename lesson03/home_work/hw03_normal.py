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



def is_parallelogram(A1: list, A2: list, A3: list, A4: list):
    """
    Функция, возвращающая True если по четырем заданным точкам можно построить параллелограм
    :param A1: список координат [x, y]
    :param A2: список координат [x, y]
    :param A3: список координат [x, y]
    :param A4: список координат [x, y]
    :return: True or False
    """

    def middle_dot(dot1, dot2):
        """
        Функция вычисляющая координаты середины отрезка из двух его точек
        :param dot1: список координат [x, y]
        :param dot2: список координат [x, y]
        :return: список координат [x, y]
        """
        x = (dot1[0] + dot2[0]) / 2
        y = (dot1[1] + dot2[1]) / 2
        return [x, y]

    dots_list = [A1, A2, A3, A4]

    # Проверка если какие-либо точки совпадают
    if any(dots_list.count(i) != 1 for i in dots_list):
        return False

    """
    По геометрии, у параллелограмма диагонали точкой пересечения делятся на 2.
    Мы не знаем порядок точек, так что попарно ищем серединную точку и записываем в список
    """
    middle_dots = []
    while len(dots_list) > 1:
        dot = dots_list.pop(0)
        for i in dots_list:
            middle_dots.append(middle_dot(dot, i))

    # Если в списке находятся две одинаковых точки, то это диагонали параллелограмма
    for d in middle_dots:
        if middle_dots.count(d) == 2:
            return True
    return False


A1 = [0, 0]
A2 = [6, 4]
A3 = [5, 0]
A4 = [1, 4]

print(is_parallelogram(A1, A2, A3, A4))


