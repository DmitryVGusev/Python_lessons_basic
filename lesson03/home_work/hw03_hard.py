# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3
def solve_fraction_equation(eq: str):
    """
    Фунцкия выполняющая операции (сложение и вычитание) с простыми дробями.
    Дроби вводятся и выводятся в формате:
    n x/y ,где n - целая часть, x - числитель, у - знаменатель.
    :param eq: строка содержащая дробное уравнение
    :return:
    """

    def parse_equation(str: str):
        """Парсит строку с уравнением и возвращает по словарю от каждой дроби"""
        str_like_list = str.split(' ')

        fract1 = {
            "n": None,
            "x": None,
            "y": None,
        }
        fract2 = fract1.copy()
        is_first = True
        while len(str_like_list) > 0:
            current = str_like_list.pop(0)
            if is_first:
                if '/' in current:
                    fract1["x"] = int(current.split('/')[0])
                    fract1["y"] = int(current.split('/')[1])
                elif current == '+':
                    is_first = False
                    is_addition = True
                elif current == '-':
                    is_first = False
                    is_addition = False
                else:
                    fract1["n"] = int(current)
            else:
                if '/' in current:
                    xy = list(map(int, current.split('/')))
                    fract2["x"] = xy[0]
                    fract2["y"] = xy[1]
                else:
                    fract2["n"] = int(current)

        for fract in [fract1, fract2]:
            if fract["n"] == None and fract["x"] == None:
                return None
            if fract["n"] == None:
                fract["n"] = 0
            if fract["y"] == 0:
                return None

        return [fract1, fract2, is_addition]




    def fract_part_unhole(fract):
        """Приведение целой части дроби в числитель"""
        return {
            "n": 0,
            "x": fract["x"] + fract["y"] * fract["n"],
            "y": fract["y"],
        }

    def fract_part_hole(fract):
        """Выделение целой части из дроби"""
        n = fract["x"] // fract["y"]
        if fract["x"] > 0:
            x = fract["x"] % fract["y"]
        else:
            x = - ((-1 * fract["x"]) % fract["y"])
        if x == 0:
            x = y = None
        else:
            y = fract["y"]

        return {"n": n, "x": x, "y": y}

    def fract_reduct(fract):
        """Сокращение дроби"""
        if fract["x"]:
            i = max(fract["x"], fract["y"])
            while i > 2:
                if fract["x"] // i != 0 and fract["y"] // i != 0:
                    fract["x"] //= i
                    fract["y"] //= i
                    break
                else:
                    i -= 1
            return fract
        else:
            return {"n": fract["n"], "x": None, "y": None}

    def fract_multiply(lst1: list, lst2: list):
        """
        Функция перемножает дроби
        :param lst1: дробь в виде списка: [числитель, знаменатель]
        :param lst2: дробь в виде списка: [числитель, знаменатель]
        :return: дробь в виде списка: [числитель, знаменатель]
        """
        result = [lst1[0]*lst2[0], lst1[1]*lst2[1]]
        return result


    def fract_sum(fract1, fract2):
        """Сложение дробей"""
        return {
            "n": 0,
            "x": fract1["x"]*fract2["y"] + fract2["x"]*fract1["y"],
            "y": fract1["y"]*fract2["y"]
        }

    def fract_sub(fract1, fract2):
        """Вычитание дробей"""
        return {
            "n": 0,
            "x": fract1["x"] * fract2["y"] - fract2["x"] * fract1["y"],
            "y": fract1["y"] * fract2["y"]
        }

    def fract_represent(fract):
        """Отображение дроби в виде строки"""
        if fract["x"]:
            result = "{} {}/{}".format(fract["n"], fract["x"], fract["y"])
        else:
            result = fract["n"]

        return result


    # Парсим входную строку, получаем две дроби и требуемую операцию над ними
    fractions = parse_equation(eq)

    fract1 = fractions[0]
    fract2 = fractions[1]
    is_addition = fractions[2]

    # Избавляемся от целых частей дроби
    fract1 = fract_part_unhole(fract1)
    fract2 = fract_part_unhole(fract2)

    # Производим сложение или вычитание в зависимости от требуемой операции
    if is_addition:
        fract3 = fract_sum(fract1, fract2)
    else:
        fract3 = fract_sub(fract1, fract2)

    return fract_represent(fract_reduct(fract_part_hole(fract3)))


# print(solve_fraction_equation("2 1/3 + 2 2/3"))
print(solve_fraction_equation("2 1/3 - 2/3"))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
