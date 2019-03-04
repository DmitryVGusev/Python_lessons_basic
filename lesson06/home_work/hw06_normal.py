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
        if len(name.split()) != 3:
            raise ValueError("Некорректное ФИО")
        self.name = name

    @property
    def short_name(self):
        """Возвращает Фамилию И.О."""
        full_name = self.name.split()
        return "{} {}.{}.".format(full_name[0], full_name[1][0], full_name[2][0])


class Student(Human):
    """Класс Ученик"""
    def __init__(self, name, parents):
        Human.__init__(self, name)

        #
        if (type(parents) not in [set, list, tuple]
            or len(parents) != 2
            or (any(type(p) != str for p in parents))
        ):
            raise ValueError("Некорректно заданы имена родителей. Корректный формат: ['ФИО1', 'ФИО2']")
        self.parents = parents

        # В каком классе учится
        self.grade = None
        # Указатель на объект школа
        self.school = None

    def get_parents_name(self):
        """Отображает ФИО родителей ученика"""
        print(f"Ученик: {self.name}. Родители: {self.parents[0]} и {self.parents[1]}.")

    def get_student_info(self):
        """Возвращает информацию об ученике
        класс, учителя, предметы"""
        if not self.school:
            print(f"{self.short_name} не учится в школе.")
        else:
            # lessons = list(filter(lambda lesson: self.grade in lesson, self.school.lessons))
            lessons = [lesson for lesson in self.school.lessons if self.grade in self.school.lessons[lesson]]
            # teachers = [teacher.name for teacher in self.school.teachers if teacher.spec in lessons]
            teachers = self.school.get_teachers_list_by_grade(self.grade)
            print("{}: ученик {} класса. \nПредметы: {}.\nУчителя: {}".format(
                self.short_name,
                self.grade,
                ', '.join(list(map(lambda teacher: teacher.spec, teachers))),
                ', '.join(list(map(lambda teacher: teacher.name, teachers)))))


class Teacher(Human):
    """Класс учитель"""
    def __init__(self, name, speciality):
        Human.__init__(self, name)
        self.spec = speciality


class School:
    """Класс школа"""

    def __init__(self):
        self.students = set()
        self.grades = set()
        # Словарь занятий. Ключ - наименование, значение - список классов в котором преподается
        self.lessons = dict()
        self.teachers = set()

    def add_grade(self, grade):
        """Добляет класс"""
        if grade in self.grades:
            print("Такой класс уже есть.")
        else:
            self.grades.add(grade)
            print(f"Класс {grade} создан.")

    def remove_grade(self, grade):
        """Роспускает класс"""
        if any(student.grade == grade for student in self.students):
            print(f"Невозможно расформировать класс {grade}: в классе есть ученики.")
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
            print(f"Учитель {teacher.name} ({teacher.spec}) зачислен в школу.")

    def fire_teacher(self, teacher: Teacher):
        """Увольняет учителя из школы"""
        if teacher not in self.teachers:
            print("Этот учитель не работает в школе.")
        if len(self.lessons[teacher.spec]) != 0:
            print(f"Невозможно уволить {teacher.short_name}. ",
                  f"Его предмет ({teacher.spec}) еще входит в учебную программу классов.")
        else:
            self.teachers.remove(teacher)

    def add_lessons(self, *lessons):
        """Добавляет предмет(ы) в школьный курс"""
        for lesson_name in lessons:
            if self.lessons.get(lesson_name):
                print(f"Предмет {lesson_name} уже в учебной программе школы.")
            else:
                self.lessons.update({lesson_name: []})
                print(f"Предмет {lesson_name} добавлен в учебную программу школы.")

    def remove_lesson(self, lesson_name):
        """Удаляет предмет из школьной программы"""
        if not self.lessons.get(lesson_name):
            print(f"Предмет {lesson_name} не входит в школьную программу.")
        elif any(t.spec == lesson_name for t in self.teachers):
            print(f"Невозможно удалить {lesson_name} из учебной программы: сначала увольте учителя.")
        else:
            self.lessons.pop(lesson_name)
            print(f"Предмет {lesson_name} удален из школьной программы.")

    def add_lesson_to_grade(self, lesson_name, grade):
        """Добавляет предмет в классную программу"""
        if grade not in self.grades:
            print(f"В школе нет {grade} класса.")
        elif lesson_name not in self.lessons:
            print(f"Предмет {lesson_name} не входит в школьную программу.")
        elif not any(t.spec == lesson_name for t in self.teachers):
            print(f"В школе нет преподавателя предмета {lesson_name}.")
        else:
            self.lessons[lesson_name].append(grade)
            print(f"Предмет {lesson_name} добавлен в учебную программу {grade} класса.")

    def remove_lesson_from_grade(self, lesson_name: str, grade: str):
        """Убирает предмет из классной программы"""
        if grade not in self.grades:
            print(f"В школе нет {grade} класса.")
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
            print(f"Данный ученик ({student.short_name}) уже учится в {student.grade} классе.")
        else:
            self.students.add(student)
            student.grade = grade
            student.school = self
            print(f"Ученик {student.short_name} зачислен в {grade} класс.")

    def remove_student(self, student: Student):
        """Отчисляет ученика из школы"""
        if student not in self.students:
            print(f"Данного ученика нет в списках школы.")
        else:
            student.grade = None
            student.school = None
            self.students.remove(student)
            print(f"Ученик {student.short_name} отчислен.")

    def set_student_to_grade(self, student: Student, grade: str):
        """Перевести школьника в класс"""
        if grade not in self.grades:
            print(f"В школе нет {grade} класса.")
        elif student.school != self:
            print(f"{student.short_name} не учится в этой школе.")
        elif student.grade == grade:
            print(f"{student.short_name} уже учится в {grade} классе.")
        else:
            student.grade = grade
            print(f"Ученик {student.short_name} переведен в {grade} класс.")

    def get_grades_list(self):
        """Отображает список классов"""
        print("Список классов:"),
        print('\n'.join(self.grades))

    def get_students_list_by_grade(self, grade: str):
        """Отображает список учеников в классе"""
        if grade not in self.grades:
            print(f"В школе нет {grade} класса.")
        else:
            students = list(filter(lambda s: s.grade == grade, self.students))
            print(f"Список учащихся {grade} класса:")
            if not students:
                print(f"Класс пуст.")
            else:
                print('\n'.join([st.short_name for st in students]))

    def _get_lessons_by_grade(self, grade: str):
        """Возвращает список предметов в классе"""
        return [l for l in self.lessons if grade in self.lessons[l]]

    def get_teachers_list_by_grade(self, grade):
        """Возвращает список учителей, преподающих в указанном классе"""
        return [t for t in self.teachers if t.spec in self._get_lessons_by_grade(grade)]

    def get_teachers_by_grade(self, grade: str):
        """Отображает список учителей, преподающих в указанном классе"""
        if grade not in self.grades:
            print(f"В школе нет {grade} класса.")
        teachers_in_grade = self.get_teachers_list_by_grade(grade)
        print(f"Список учителей, преподающих в {grade} классе:")
        if not teachers_in_grade:
            print(f"В {grade} классе никто не преподает.")
        else:
            print('\n'.join(list(map(lambda teacher: teacher.name, teachers_in_grade))))


if __name__ == '__main__':

    # Создаем учителей
    math_teacher = Teacher("Алгебров Иван Иванович", "Алгебра")
    chem_teacher = Teacher("Химиков Петр Петрович", "Химия")
    geo_teacher = Teacher("Глобус Сидр Сидрович", "География")

    # Создаем учеников
    st1 = Student("Семенов Семен Васильевич", ["Семенов Василий Николаевич", "Семенова Ирина Петровна"])
    st2 = Student("Алабина Анастасия Макаровна", ["Алабин Макар Олегович", "Алабина Светлана Юрьевна"])
    st3 = Student("Карпов Петр Васильевич", ["Карпова Мария Семеновна", "Карпов Василий Олегович"])

    # Создаем школу и предметы
    print()
    school = School()
    school.add_lessons("Биология", "Алгебра", "Химия", "География")

    # Создаем классы и добавляем в них учеников
    print()
    school.add_grade("5A")
    school.add_grade("5B")
    school.add_grade("6A")
    school.add_grade("8A")
    school.add_student(st1, "5A")
    school.add_student(st2, "7B")  # Такого класса нет. Не добавится
    school.add_student(st2, "5A")
    school.add_student(st3, "5A")
    school.set_student_to_grade(st3, "5B")

    # Нанимаем учителей
    print()
    school.hire_teacher(math_teacher)
    school.hire_teacher(chem_teacher)
    school.hire_teacher(geo_teacher)
    school.hire_teacher(geo_teacher)

    # Добавляем предметы в учебную программу класса
    print()
    school.add_lesson_to_grade("Алгебра", "5A")
    school.add_lesson_to_grade("Алгебра", "5B")
    school.add_lesson_to_grade("Алгебра", "6A")
    school.add_lesson_to_grade("Биология", "5A")
    school.add_lesson_to_grade("Биология", "5В")
    school.add_lesson_to_grade("Химия", "6A")
    school.add_lesson_to_grade("География", "5A")

    # 1. Получить полный список всех классов школы
    print()
    school.get_grades_list()

    # 2. Получить список всех учеников в указанном классе
    print()
    school.get_students_list_by_grade("6A")  # Класс пуст
    school.get_students_list_by_grade("7A")  # Такого класса нет
    school.get_students_list_by_grade("5A")

    # 3. Получить список всех предметов указанного ученика
    print()
    st1.get_student_info()

    # 4. Узнать ФИО родителей указанного ученика
    print()
    st2.get_parents_name()

    # 5. Получить список всех Учителей, преподающих в указанном классе
    print()
    school.get_teachers_by_grade("5A")
    school.get_teachers_by_grade("8A")  # В 8A классе никто не преподает.
