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


class Employee:
    """Класс сотрудник"""
    # Список созданных объектов класса Employee
    employees = []

    def __init__(self, raw_line: str):
        employee_data = raw_line.split()
        self.first_name = employee_data[0]
        self.last_name = employee_data[1]
        self.salary = int(employee_data[2])
        self.position = employee_data[3]
        self.hours_expected = int(employee_data[4])
        self.hours_worked_out = None
        self.income = None
        self.employees.append(self)

        pass

    @staticmethod
    def add_hours(raw_line: str):
        """
        Добавить количество отработанных часов.
        Строка на вход парсится.
        Если она является строкой с И.О. сотрудника и его отработанными часами - ищется подходящий объект
        с тим же И.О. и добавляется информация об отработанных часах.
        :param raw_line: строка, содержащая И.О. сотрудника и количество отработанных часов
        :return: None
        """
        # Парсим строку
        worker_hours = raw_line.split()
        first_name = worker_hours[0]
        last_name = worker_hours[1]
        hours_worked_out = int(worker_hours[2])

        for worker in Employee.employees:
            if first_name == worker.first_name and last_name == worker.last_name:
                worker.hours_worked_out = hours_worked_out
                worker.calculate_salary()
                return

    @staticmethod
    def employees_info():
        """Отображает информацию о всех сотрудникаф: Ф.И, должность, оклад, отработано, ЗП"""
        print("{:18} {:^12} {:^10} {:10} {:^6}".format("Ф.И.", "Должность", "Оклад", "Отработано", "ЗП"))
        for emp in Employee.employees:
            print("{:18} {:12} {:^10} {:^10} {:0.2f}".format(
                f"{emp.last_name} {emp.first_name}",
                emp.position,
                emp.salary,
                emp.hours_worked_out,
                emp.income
            ))

    def calculate_salary(self):  # TODO реализовать метод
        """Высчитать зарплату сотрудника за месяц"""
        # Почасовой оклад
        per_hour_salary = self.salary / self.hours_expected
        if self.hours_expected >= self.hours_worked_out:
            # Сумма за отработанные часы до нормы
            self.income = self.hours_worked_out * per_hour_salary
        else:
            # Сумма за отработанные часы сверх нормы
            # xp + 2p(y-x) = p(2y - x), где x - норма, y - выработка, p - per_hour salary
            self.income = per_hour_salary * (2 * self.hours_worked_out - self.hours_expected)

    def get_info(self):
        """Отображает информацию о сотруднике"""


if __name__ == '__main__':

    # Считываем базовую информацию о рабочих
    with open("data/workers", 'r', encoding='utf-8') as f:
        f.readline()
        for line in f.readlines():
            Employee(line.strip())

    # Считываем информацию об отработанных часах
    with open("data/hours_of", 'r', encoding='utf-8') as f:
        f.readline()
        for line in f.readlines():
            Employee.add_hours(line.strip())

    # Отображаем расчетную зарплату по всем сотрудникам
    Employee.employees_info()


