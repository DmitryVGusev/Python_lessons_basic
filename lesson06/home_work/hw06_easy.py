# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import sqrt, sin, acos, degrees


class Figure:
    """Класс геометрическая фигура"""

    def __init__(self, *args):
        self.a = "a"
        self.coords = []
        for el in args:
            if self.is_coodrinate_valid(el):
                self.coords.append(tuple(el))
        self.sides = [self.get_side(self.coords[i], self.coords[i+1]) for i in range(-len(self.coords), 0)]


    def get_perimeter(self):
        """Возвращает перимерт фигуры"""
        return round(sum(self.sides), 2)


    @staticmethod
    def is_coodrinate_valid(coord):
        """Проверяет координаты на валидность"""
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




"""
Поскольку не ясно, выбирает ли высоту пользователь или берется любая по усмотрению разработчика,
решено было пойти по первому пути
"""


class Triangle:
    """Класс треугольник"""

    def __init__(self, a, b, c):
        # Проверка входных параметров
        # Координаты каждой точки должны состоять из двух элементов
        for el in [a, b, c]:
            if type(el) not in [tuple, list] or len(el) != 2:
                raise TypeError(f"{el} <-- Координаты точек должны быть формата (x,y)")
            # Элементы координат должны быть числами
            for i in el:
                if type(i) not in [int, float]:
                    raise TypeError(f"{el} <-- Координаты точек должны быть числами")

        # Хранит координаты точек
        self.coords = (a, b, c)

        # Хранит длины сторон
        self.sides = [self._get_side(ind) for ind in [-3, -2, -1]]

        # Хранит велечины углов в радианах
        self.angles = [self._get_angle(ind) for ind in [-3, -2, -1]]

    def _get_side(self, ind):
        """Возвращает длину стороны труегольника"""
        return sqrt(
            (self.coords[ind][0] - self.coords[ind+1][0])**2 +
            (self.coords[ind][1] - self.coords[ind+1][1])**2
        )

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

    def get_perimeter(self):
        """Возвращает перимерт треугольника"""
        return sum(self.sides)

    def get_square(self):
        """Вычисляет площадь треугольника"""
        return round(self.get_height(0) * self.sides[1] / 2, 5)


# if __name__ == '__main__':
    # triangle = Triangle([1, "0"], [2, 0], [0, 0])
    # egipt_triangle = Triangle([0, 0], [0, 3], [4, 0])
    # print(egipt_triangle.sides)
    # print(list(map(degrees, egipt_triangle.angles)))
    # print(egipt_triangle.get_height(0))
    # print(egipt_triangle.get_square())
    # print(triangle.get_perimeter())


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
    # equi = EquiTrapezium([0, 0], [1, 3], [3, 3], [4, 0])
    equi = EquiTrapezium([3,0], [0,1], [0,3], [3, 4])
    print(equi.is_equi_trapezium())
    print(equi.get_perimeter())
    print(equi.get_square())