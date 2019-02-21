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
    :return: строка содержащая дробь
    """

    def parse_equation(str: str):
        """
        Парсит строку с уравнением в список из двух дробей
        :param str: Строка с уравнением
        :return:
        """
        str_like_list = str.split(' ')
        first_part = True
        fract1 = []
        fract2 = []
        while len(str_like_list) > 0:
            current = str_like_list.pop(0)
            if first_part:
                if current == '+':
                    operation = 'add'
                    first_part = False
                    continue
                if current == '-':
                    operation = 'sub'
                    first_part = False
                    continue
                if '/' not in current:
                    fract1.append([int(current), 1])
                else:
                    fract1.append(list(map(int, current.split('/'))))
            else:
                if '/' not in current:
                    fract2.append([int(current), 1])
                else:
                    fract2.append(list(map(int, current.split('/'))))

        # Проверка дробей на валидность и подготовка перед выводом
        result = []
        for fract in fract1, fract2:
            #  Если в списке дроби не один или два элемента, то парсинг прошел некорректно и нужно выдать ошибку
            if len(fract) not in [1, 2]:
                return None
            elif len(fract) == 2:
                # Приведение целой части в числитель
                fract_new = fract_sum(fract[0], fract[1])
                fract = fract_new
            else:
                fract= fract[0]
            result.append(fract)

        result.append(operation)
        return result

    def fract_multiply(lst1: list, lst2: list):
        """
        Функция перемножает дроби
        :param lst1: дробь в виде списка: [числитель, знаменатель]
        :param lst2: дробь в виде списка: [числитель, знаменатель]
        :return: дробь в виде списка: [числитель, знаменатель]
        """
        result = [lst1[0]*lst2[0], lst1[1]*lst2[1]]
        return result

    def fract_sum(f1, f2):
        """
        Сложение дробей
        :param f1: дробь в виде списка: [числитель, знаменатель]
        :param f2: дробь в виде списка: [числитель, знаменатель]
        :return: дробь в виде списка: [числитель, знаменатель]
        """
        return [f1[0]*f2[1] + f1[1]*f2[0], f1[1]*f2[1]]

    def fract_sub(f1, f2):
        """
        Вычитание дробей
        :param f1: дробь в виде списка: [числитель, знаменатель]
        :param f2: дробь в виде списка: [числитель, знаменатель]
        :return: дробь в виде списка: [числитель, знаменатель]
        """
        return [f1[0]*f2[1] - f1[1]*f2[0], f1[1]*f2[1]]

    def fract_represent(f):
        """
        Отображение дроби в виде строки.
        Перед отображением идет сокращение и выделение целой части из дроби
        :param f: дробь в виде списка: [числитель, знаменатель]
        :return:
        """

        # Если числитель отрицательный - приводим к положительному.
        # Это позволит пользоваться делением от остатка.
        if f[0] < 0:
            sign = -1
            f[0] *= -1
        else:
            sign = 1

        # Сокращение дроби.
        # Ищем максимальный общий делитель. Перебираем по низпадающей до 1
        i = min(f)
        while i > 1:
            if f[0] % i == 0 and f[1] % i == 0:
                f[0] //= i
                f[1] //= i
                break
            i -= 1

        # Выделение целой части
        hole = f[0] // f[1]
        f[0] %= f[1]

        # Вывод с целой частью или без. Приводим к отрицательному если был
        if hole != 0:
            result = "{} {}/{}".format(hole * sign, f[0], f[1])
        else:
            result = "{}/{}".format(f[0] * sign, f[1])

        return result


    # Парсим входную строку, получаем две дроби и требуемую операцию над ними
    fractions = parse_equation(eq)

    fract1 = fractions[0]
    fract2 = fractions[1]
    operation = fractions[2]

    # Производим сложение или вычитание в зависимости от требуемой операции
    if operation == 'add':
        fract3 = fract_sum(fract1, fract2)
    else:
        fract3 = fract_sub(fract1, fract2)

    # Выводим результат
    return fract_represent(fract3)


# print(solve_fraction_equation("5/6 + 4/7"))
# print(solve_fraction_equation("-2/3 - -2"))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
"""
Сделаем допущение, что структура файлов верна, выбраковывать строки не надо,
и о каждом сотруднике есть информация в обоих файлах 
"""

def form_working_hours(workers_file: str, hours_of_file: str):
    """
    Функция расчитывает зарплату сотрудников, основываясь на таблице расчета зп собтрудников
    и таблице отработанных часов сотрудниками
    :param workers_file: путь до файла с таблицей расчета ЗП
    :param hours_of_file: путь до файла с таблицей отработанных часов
    :return: таблица рассчета итоговой зарплаты
    """

    # Считаем информацию из файлов и сложим в сыром виде
    with open(workers_file, "r") as w:
        workers_raw = w.readlines()

    with open(hours_of_file, "r") as h:
        hours_raw = h.readlines()

    # Обрабатываем общую информацию о сотрудниках
    workers = dict()
    workers_raw.pop(0)
    for i in workers_raw:
        line_raw = i.replace('\n', '').split()
        workers[' '.join([line_raw[1], line_raw[0]])] = [
            int(line_raw[2]),
            line_raw[3],
            int(line_raw[4])
        ]

    # Обрабатываем информацию об отработанных часах
    hours_raw.pop(0)
    for i in hours_raw:
        line_raw = i.replace('\n', '').split()
        worker_name = ' '.join([line_raw[1], line_raw[0]])
        if worker_name in workers:
            workers[worker_name].append(int(line_raw[2]))

    """
    Структура словаря workers
    "Фамилия Имя" : [
            Должность,
            Оклад,
            Норма часов,
            Отработанные часы]
    """

    # Подсчет часов
    for key in workers.keys():
        # Зарплата за час
        per_hour_salary = workers[key][0] / workers[key][2]

        if workers[key][2] >= workers[key][3]:
            # Сумма за отработанные часы до нормы
            income = workers[key][3] * per_hour_salary
        else:
            # Сумма за отработанные часы сверх нормы
            # xp + 2p(y-x) = p(2y - x), где x - норма, y - выработка, p - per_hour salary
            income = per_hour_salary * (2 * workers[key][3] - workers[key][2])
        # Добавляем зарплату в список значений элементов словаря workers
        workers[key].append(income)

    # Вывод результатов
    print("{:18} {:^12} {:^10} {:10} {:^6}".format("Ф.И.", "Должность", "Оклад", "Отработано", "ЗП"))
    for key in workers.keys():
        print("{:18} {:12} {:^10} {:^10} {:0.2f}".format(
            key,
            workers[key][1],
            workers[key][0],
            workers[key][3],
            workers[key][4]
        ))

    return True

workers_file = 'data/workers'
hours_of_file = 'data/hours_of'
form_working_hours(workers_file, hours_of_file)


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
