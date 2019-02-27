#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

from os import chdir
from lesson05.home_work import hw05_easy


def shell_cd(path):
    """Сменяет текущую директорию на указанную"""
    try:
        chdir(path)
        print("Успешно перешел")
    except:
        print("Невозможно перейти")


if __name__ == '__main__':
    print("Добро пожаловать в командную оболочку pysh")
    while True:
        print("\nВыберите действие:\n" +
              "1. Перейти в папку\n" +
              "2. Просмотреть содержимое текущей папки\n" +
              "3. Удалить папку\n" +
              "4. Создать папку\n" +
              "0. Выход")

        choise = input("[1-4]?: ")
        if choise == "1":
            dirname = input("Укажите директорию: ")
            shell_cd(dirname)
        elif choise == "2":
            hw05_easy.shell_ls()
        elif choise == "3":
            dirname = input("Укажите имя директории: ")
            hw05_easy.shell_rmdir(dirname)
        elif choise == "4":
            dirname = input("Укажите имя директории: ")
        elif choise == '0':
            print("Завершение работы командной оболочки")
            break
        else:
            print("Неизвестное действие")
