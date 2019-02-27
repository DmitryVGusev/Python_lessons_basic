#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import mkdir, rmdir
from os import listdir
from os.path import isdir

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def shell_mkdir(dirname):
    try:
        mkdir(dirname)
        print(f"Директория {dirname} успешно создана.")
    except FileExistsError:
        print(f"Невозможно создать директорию {dirname}: директория уже существует")
    except:
        print(f"Невозможно создать директорию {dirname}.")


def shell_rmdir(dirname):
    try:
        rmdir(dirname)
        print(f"Директория {dirname} успешно удалена.")
    except FileNotFoundError:
        print(f"Невозможно удалить директорию {dirname}: директории не существует")
    except:
        print(f"Невозможно удалить директорию {dirname}.")


# Проверка результатов
if __name__ == "__main__":
    # Создание директории dir_1 - dir_9 в папке
    for i in range(1, 10):
        shell_mkdir(f"dir_{i}")

    # Удаление директории dir_1 - dir_9 в папке
    for i in range(1, 10):
        shell_rmdir(f"dir_{i}")


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def shell_ls(path=".", cmd_line: str=''):
    """Отображает список файлов в текущей директории"""
    curr_dir_contents = listdir(path)
    if "-d" in cmd_line:
        for file in curr_dir_contents:
            if isdir(file):
                print(file)
    else:
        for file in curr_dir_contents:
            print(file)


# Проверка результатов
if __name__ == "__main__":
    # Отображение папок в текущей директории
    shell_ls(path=".", cmd_line='-d')


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
from shutil import copy


def shell_cp(src: str, dst: str):
    """Копирует заданный файл"""
    try:
        copy(src, dst)
        print(f"Скопирован: {src} -> {dst}")
    except:
        print(f"Не удалось скопировать {src} -> {dst}")


# Проверка результатов
if __name__ == "__main__":
    shell_cp(__file__, __file__ + "_copy")
