#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import sqrt, sin, acos, degrees


class Figure:
    """Класс геометрическая фигура"""

    def __init__(self, *args):
        # Переменная со списком координат
        self.coords = []
        for el in args:
            if self.is_valid_coodrinate(el):
                self.coords.append(tuple(el))

        # Проверка на несовпадающие координаты
        if len(set(self.coords)) != len(args):
            raise Exception("Координаты не должны совпадать")

        self.sides = [self.get_side(self.coords[i], self.coords[i+1]) for i in range(-len(self.coords), 0)]

    def get_perimeter(self):
        """Возвращает сумму длин фигуры"""
        return round(sum(self.sides), 2)

    @staticmethod
    def is_valid_coodrinate(coord):
        """
        Проверяет координаты на валидность.
        Координата должна быть в виде кортежа или списка и содержать в себе два числа
        """
        # Координаты каждой точки должны состоять из двух элементов
        if type(coord) not in [tuple, list] or len(coord) != 2:
            raise TypeError(f"{coord} <-- Координаты точек должны быть формата (x,y)")
        # Элементы координат должны быть числами
        for i in coord:
            if type(i) not in [int, float]:
                raise TypeError(f"{coord} <-- Координаты точек должны быть числами")
        return True

    @staticmethod
    def get_side(coord1, coord2):
        """Возвращает длину отрезка между двумя точками"""
        return sqrt(
            (coord1[0] - coord2[0])**2 +
            (coord1[1] - coord2[1])**2
        )


class Triangle(Figure):
    """Класс треугольник"""

    def __init__(self, a, b, c):
        Figure.__init__(self, a, b, c)

        # Хранит велечины углов в радианах
        self.angles = [self._get_angle(ind) for ind in [-3, -2, -1]]

        # Проверка что точки не находятся на одной прямой
        if any(angle == 0 for angle in self.angles):
            raise Exception("Точки не должны лежать на одной прямой")

    def _get_angle(self, ind):
        """Возвращает угол в градусах"""
        cos_x = (
            (self.sides[ind] ** 2 + self.sides[ind+2] ** 2 - self.sides[ind+1] ** 2) /
            (2 * self.sides[ind] * self.sides[ind+2])
        )
        return acos(cos_x)

    def get_height(self, ind: int):
        """
        Возвращает высоту треугольника
        :param ind: номер угла, по порядку введенных координат (0-2)
        :return: высота выходящая из заданного угла
        """
        # Проверка корректности входных данных
        if type(ind) is not int or ind not in range(2):
            raise IndexError('Индекс угла должен быть задан целым числом в пределах [0-2]')

        return self.sides[ind-1] * sin(self.angles[ind-1])

    def get_square(self):
        """Вычисляет площадь треугольника"""
        return round(self.get_height(0) * self.sides[1] / 2, 2)


# Проверка результатов
if __name__ == '__main__':
    egipt_triangle = Triangle([0, 0], [0, 3], [4, 0])
    print(f"Стороны египетского треугольника: {egipt_triangle.sides}")
    print(f"Углы египеткого треугольника: {list(map(degrees, egipt_triangle.angles))}")
    print(f"Высота : {egipt_triangle.get_height(0)}")
    print(f"Площадь егопетского треугольника: {egipt_triangle.get_square()}")
    print(f"Периметр египетского треугольника: {egipt_triangle.get_perimeter()}")


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class EquiTrapezium(Figure):
    num_of_sides = 4

    def __init__(self, a, b, c, d):
        Figure.__init__(self, a, b, c, d)
        if len(set(self.coords)) != self.num_of_sides:
            raise ValueError("Неверное количество точек либо совпадающие точки")

    def is_equi_trapezium(self):
        """Возвращает True если фигура является равнобочной тропецией"""
        # Сравнивается равенство диагоналей и противоположных сторон
        if (self.get_side(self.coords[0], self.coords[2]) == self.get_side(self.coords[1], self.coords[3])
                and self.sides[0] == self.sides[2] or self.sides[1] == self.sides[3]):
            return True
        else:
            return False

    def get_square(self):
        """Вычисляет прощадь равнобочной трапеции"""

        # Если фигура не является равнобочной трапецией, выкидывает исключение
        if not self.is_equi_trapezium():
            raise Exception("Фигура не является равнобочной трапецией. Вычисление площади невозможно")

        # Определяются бока трапеции и основения
        if self.sides[0] == self.sides[2]:
            a = min(self.sides[1], self.sides[3])
            b = max(self.sides[1], self.sides[3])
            c = self.sides[0]
        else:
            a = min(self.sides[0], self.sides[2])
            b = max(self.sides[0], self.sides[2])
            c = self.sides[1]

        square = (a + b) / 2 * sqrt(c**2 - (b - a)/2)
        return round(square, 2)


# Проверка результатов
if __name__ == '__main__':
    print()
    equi = EquiTrapezium([3, 0], [0, 1], [0, 3], [3, 4])
    print(f"Стороны трапеции: {equi.sides}")
    print(f"Является ли равнобочной трапецией: {equi.is_equi_trapezium()}")
    print(f"Периметр трапеции: {equi.get_perimeter()}")
    print(f"Площадь равнобочной трапеции: {equi.get_square()}")
