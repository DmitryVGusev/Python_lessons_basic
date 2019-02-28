#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции) (про удаление директории не сказано)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
import sys
from os import getcwd, remove
import hw05_easy
import hw05_normal

def print_help(*args):
    print("help - получение справки")
    print("mkdir <dir_name> - создать директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создать копию указанного файла")
    print("rm <file_name> - удалить указанный файл")
    print("cd <full_path or relative_path> - сменить текущую директорию на указанную")
    print("ls - отобразить полный путь текущей директории")
    print("ping - тестовый ключ")


def shell_rm(filename):
    """Удаляет указанный файл"""

    if not filename:
        print("Укажите имя файла для удаления!")
        return None

    answer = input(f"Вы действительно хотите удалить {filename} [y/n]? ")
    if answer.lower() in ['y', 'yes']:
        try:
            remove(filename)
            print(f"Файл {filename} успешно удален.")
        except FileNotFoundError:
            print(f"Невозможно удалить {filename}: файл не найден")
        except PermissionError:
            print(f"Нет прав на удаление {filename}!")
        except OSError:
            print("Невозможно удалить директорию!")
        except:
            print(f"Не удалось удалить файл {filename}!")


def shell_pwd(*args):
    """Возвращает полный путь текущей директории"""
    print(getcwd())


def ping(*args):
    print("pong")


#
do = {
    "help": print_help,
    "mkdir": hw05_easy.shell_mkdir,
    "ping": ping,
    "cp": hw05_easy.shell_cp,
    "rm": shell_rm,
    "cd": hw05_normal.shell_cd,
    "ls": shell_pwd
}

if __name__ == '__main__':
    # Парсим первый аргумент
    try:
        key = sys.argv[1]
    except IndexError:
        key = None

    # Парсим второй аргумент
    try:
        arg = sys.argv[2]
    except IndexError:
        arg = None

    if key:
        if do.get(key):
            do[key](arg)
        else:
            print("Задан неверный ключ")
            print("Укажите ключ help для получения справки")
    else:
        print("Укажите ключ help для получения справки")
