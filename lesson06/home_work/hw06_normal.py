# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Human:
    """Класс Человек"""
    def __init__(self, name: str):
        self.name = name

    @property
    def short_name(self):
        """Возвращает Фамилию И.О."""
        full_name = self.name.split()
        return "{} {}.{}.".format(full_name[0], full_name[1][0], full_name[2][0])


class Student(Human):
    """Класс Ученик"""
    def __init__(self, name, parents, grade=None):  # TODO реализовать проверку входных параметров
        Human.__init__(self, name)
        self.parents = parents
        self.grade = grade

        # Указатель на объект школа
        self.school = None

    def get_parents_name(self):
        """Отображает ФИО родителей ученика"""
        print(f"Ученик: {self.name}. Родители: {self.parents[0]} и {self.parents[1]}")

    def get_student_info(self):
        """Возвращает информацию об ученике
        класс, учителя, предметы"""
        if not self.school:
            print(f"{self.short_name} не учится в школе")
        else:
            # lessons = list(filter(lambda lesson: self.grade in lesson, self.school.lessons))
            lessons = [lesson for lesson in self.school.lessons if self.grade in self.school.lessons[lesson]]
            teachers = [teacher for teacher in self.school.teachers if teacher.spec in lessons]
            print("{}: ученик {} класса. \nПредметы: {}.\n Учителя: {}\n".format(
                self.short_name,
                self.grade,
                ' '.join(map(str, lessons)),
                ' '.join(map(str, teachers))
            ))


class Teacher(Human):
    """Класс учитель"""
    def __init__(self, name, speciality):
        Human.__init__(self, name)
        self.spec = speciality


class School:
    """Класс школа"""

    def __init__(self, name):  # TODO реализовать проверку входных параметров
        self.students = set()
        self.grades = set()
        # Словарь занятий. Ключ - наименование, значение - список классов в котором преподается
        self.lessons = dict()
        self.teachers = set()

    def add_grade(self, grade):
        """Добавить класс"""
        if grade in self.grades:
            print("Такой класс уже есть")
        else:
            self.grades.add(grade)
            print(f"Класс {grade} создан.")

    def remove_grade(self, grade):
        """Распустить класс"""
        if any(student.grade == grade for student in self.students):
            print(f"Невозможно расформировать класс {grade}: в классе есть ученики")
        else:
            self.grades.remove(grade)
            print(f"Класс {grade} успешно расформирован.")

    def hire_teacher(self, teacher: Teacher):
        """Нанимает учителя в школу"""
        if teacher in self.teachers:
            print("Этот учитель уже работает в школе.")
        elif any(t.spec == teacher.spec for t in self.teachers):
            print(f"Невозможно нанять учителя. Данный предмет ({teacher.spec}) уже преподает другой учитель.")
        else:
            self.teachers.add(teacher)

    def fire_teacher(self, teacher: Teacher):  # TODO реализовать данный метод
        """Увольняет учителя из школы"""
        if teacher not in self.teachers:
            print("Этот учитель не работает в школе")
        if len(self.lessons[teacher.spec]) != 0:
            print(f"Невозможно уволить {teacher.short_name}. ",
                  f"Его предмет ({teacher.spec}) еще входит в учебную программу классов")
        else:
            self.teachers.remove(teacher)

    def add_lessons(self, *lessons):
        """Добавить предмет(ы) в школьный курс"""
        for lesson_name in lessons:
            if self.lessons.get(lesson_name):
                print(f"Предмет {lesson_name} уже в учебной программе школы.")
            else:
                self.lessons.update({lesson_name: []})
                print(f"Предмет {lesson_name} добавлен в учебную программу школы.")

    def remove_lesson(self, lesson_name):
        """Удаляет предмет из школьной программы"""
        if not self.lessons.get(lesson_name):
            print(f"Предмет {lesson_name} не входит в школьную программу")
        elif any(t.spec == lesson_name for t in self.teachers):
            print(f"Невозможно удалить {lesson_name} из учебной программы: сначала увольте учителя.")
        else:
            self.lessons.pop(lesson_name)
            print(f"Предмет {lesson_name} удален из школьной программы.")

    def add_lesson_to_grade(self, lesson_name, grade):
        """Добавляет предмет в классную программу"""
        if grade not in self.grades:
            print(f"В школе нет {grade} класса")
        elif lesson_name not in self.lessons:
            print(f"Предмет {lesson_name} не входит в школьную программу.")
        elif not any(lambda t: t.spec == lesson_name, self.teachers):
            print(f"В школе нет преподавателя предмета {lesson_name}.")
        else:
            self.lessons[lesson_name].append(grade)
            print(f"Предмет {lesson_name} добавлен в учебную программу {grade} класса")

    def remove_lesson_from_grade(self, lesson_name: str, grade: str):
        """Убрать предмет из классной программы"""
        if grade not in self.grades:
            print(f"В школе нет {grade} класса")
        elif lesson_name not in self.lessons:
            print(f"Предмет {lesson_name} не входит в школьную программу.")
        elif lesson_name not in self.lessons[lesson_name]:
            print(f"Предмет {lesson_name} не входит в программу {grade} класса.")
        else:
            self.lessons[lesson_name].remove(grade)
            print(f"Предмет {lesson_name} удален из учебной программы {grade} класса.")

    def add_student(self, student: Student, grade: str):
        """Добавляет ученика в школу"""
        if grade not in self.grades:
            print(f"В школе нет {grade} класса.")
        elif student in self.students:
            print(f"Данный ученик уже учится в {student.grade} классе.")
        else:
            self.students.add(student)
            student.grade = grade
            print(f"Ученик {student.short_name} зачислен в {grade} класс")

    def remove_student(self, student: Student):
        """Отчисляет ученика из школы"""
        if student not in self.students:
            print(f"Данного ученика нет в списках школы.")
        else:
            student.grade = None
            self.students.remove(student)
            print(f"Ученик {student.short_name} отчислен.")

    def set_student_to_grade(self, student: Student, grade: str):  # TODO обработать исключения
        """Перевести школьника в класс"""
        student.grade = grade
        print(f"{student.short_name} переведен в {grade} класс")

    def get_grades_list(self):  # TODO оформить вывод
        """Возвращает список классов"""
        return self.grades

    def get_students_list_by_grade(self, grade: str):  # TODO оформить вывод
        """Возвращает список учеников в классе"""
        return list(filter(lambda s: s.grade == grade, self.students))

    def get_lessons_by_grade(self, grade):
        """Возвращает список предметов в классе"""
        return list(filter(lambda l: grade in l, self.lessons))

    def get_teachers_list_by_grade(self, grade):
        """Возвращает список учителей, преподающих в классе"""
        return [t for t in self.teachers if t.spec in self.get_lessons_by_grade(grade)]


if __name__ == '__main__':  # TODO реализовать проверку результатов
    pass