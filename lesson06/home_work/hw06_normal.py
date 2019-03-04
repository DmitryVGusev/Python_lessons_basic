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
    def __init__(self, name):
        self.name = name

    @property
    def short_name(self):  # TODO реализовать данный метод
        """Возвращает Фамилию И.О."""
        pass


class Student(Human):
    """Класс Ученик"""
    def __init__(self, name, parents, grade=None):
        Human.__init__(self, name)
        self.parents = parents
        self.grade = grade

    def get_parents_name(self):  # TODO реализовать данный метод
        """Возвращает ФИО родителей ученика"""
        pass


class Teacher(Human):
    """Класс учитель"""
    def __init__(self, name, speciality):
        Human.__init__(self, name)
        self.spec = speciality


class School:
    """Класс школа"""
    class Lesson:
        """Вложенный класс предмет. Используется внутри класса школы"""
        def __init__(self, name):
            self.name = name
            self.grades = []
            self.teacher = None

    def __init__(self, name):  # TODO реализовать проверку входных параметров
        self.students = set()
        self.grades = set()
        self.lessons = set()
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
            # Закрепим преподавателя за предметом
            spec_lesson = list(filter(lambda l: l.name == teacher.spec, self.teachers))[0]
            spec_lesson.teacher = teacher

    def fire_teacher(self, teacher):  # TODO реализовать данный метод
        """Увольняет учителя из школы"""
        pass

    def add_lessons(self, *lessons):
        """Добавить предмет(ы) в школьный курс"""
        for lesson_name in lessons:
            if any(l.name == lesson_name for l in self.lessons):
                print(f"Предмет {lesson_name} уже в учебной программе школы.")
            else:
                self.lessons.add(School.Lesson(name=lesson_name))
                print(f"Предмет {lesson_name} добавлен в учебную программу школы.")

    def remove_lesson(self, lesson_name):
        """Удаляет предмет из школьной программы"""
        if any(t.spec == lesson_name for t in self.teachers):
            print(f"Невозможно удалить {lesson_name} из учебной программы: сначала увольте учителя.")
        else:
            self.lessons.remove([l for l in self.lessons if l.name == lesson_name][0])
            print(f"Предмет {lesson_name} удален из школьной программы.")

    def add_student(self, student: Student, grade):
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

    def set_student_to_grade(self, student: Student, grade):
        """Перевести школьника в класс"""
        student.grade = grade
        print(f"{student.short_name} переведен в {grade} класс")

    def get_grades_list(self):
        """Возвращает список классов"""
        return self.grades  # TODO оформить вывод

    def get_students_list_by_class(self, grade):
        """Возвращает список учеников в классе"""
        # TODO оформить вывод
        return list(filter(lambda s: s.grade == grade, self.students))

    def get_teachers_list_by_class(self, grade):  # TODO реализовать данный метод
        """Возвращает список учителей, преподающих в классе"""
        return

if __name__ == '__main__':
    # TODO реализовать проверку результатов
    pass