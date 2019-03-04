# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла
"""
Сделаем допущение, что структура файлов верна, выбраковывать строки не надо,
и о каждом сотруднике есть информация в обоих файлах
"""


class Workers:
    """Класс рабочий"""
    # Список созданных объектов класса Worker
    workers = []

    def __init__(self, raw_line: str):
        worker_data = raw_line.split()
        self.first_name = worker_data[0]
        self.last_name = worker_data[1]
        self.salary = int(worker_data[2])
        self.position = worker_data[3]
        self.hours_expected = int(worker_data[4])
        self.workers.append(self)
        pass

    @staticmethod
    def add_hours(raw_line: str):
        """
        Добавить количество отработанных часов.
        Строка на вход парсится.
        Если она является строкой с И.О. рабочего и его отработанными часами - ищется подходящий объект
        с тим же И.О. и добавляется информация об отработанных часах.
        :param raw_line: строка, содержащая И.О. рабочего и количество отработанных часов
        :return: None
        """
        worker_hours = raw_line.split()
        # TODO реализовать метод
        pass

    def calculate_salary(self):  # TODO реализовать метод
        """Высчитать зарплату за месяц"""
        pass


if __name__ == '__main__':
    with open("data/workers", 'r', encoding='utf-8') as f:
        f.readline()
        for line in f.readlines():
            Workers(line.strip())

    with open("data/hours_of", 'r', encoding='utf-8') as f:
        f.readline()
        for line in f.readlines():
            Workers.add_hours(line.strip())


