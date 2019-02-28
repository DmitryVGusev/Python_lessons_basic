#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import mkdir, rmdir
from os import listdir
from os.path import isdir

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def shell_mkdir(dirname=None):
    """Создает директорию с заданным именем"""
    if not dirname:
        print("Необходимо указать имя директории!")
        return None

    try:
        mkdir(dirname)
        print(f"Директория {dirname} успешно создана.")
    except FileExistsError:
        print(f"Невозможно создать директорию {dirname}: директория уже существует")
    except:
        print(f"Невозможно создать директорию {dirname}.")


def shell_rmdir(dirname=None):
    """Удаляет директорию с заданным именем"""
    if not dirname:
        print("Необходимо указать имя директории!")
        return None

    try:
        rmdir(dirname)
        print(f"Директория {dirname} успешно удалена.")
    except PermissionError:
        print(f"Нет прав на удаление {dirname}!")
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


def shell_ls(path=".", dirs_only=False):
    """
    Отображает список файлов в текущей директории
    :param path: Абсолютный или относительный путь
    :param dirs_only: Отображать только директории в случае True
    """
    try:
        curr_dir_contents = listdir(path)
    except TypeError:
        print("Укажите корректный путь")
        return None
    except:
        print("Невозможно получить список файлов в текущей директории")
        return None
    # С ключем dirs_only оторбажает лишь директории
    if dirs_only:
        for file in curr_dir_contents:
            if isdir(file):
                print(file)
    else:
        for file in curr_dir_contents:
            print(file)


# Проверка результатов
if __name__ == "__main__":
    # Отображение папок в текущей директории
    shell_ls(".", dirs_only=True)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
from shutil import copy


def shell_cp(src: str):
    """Копирует заданный файл"""
    if not src:
        print("Необходимо указать имя файла")

    dst = src + "_copy"
    try:
        copy(src, dst)
        print(f"Скопирован: {src} -> {dst}")
    except PermissionError:
        print(f"Нет прав на копирование {src}!")
    except FileNotFoundError:
        print(f"Не удалось скопировать {src}: файл не найден")
    except:
        print(f"Не удалось скопировать {src} -> {dst}")


# Проверка результатов
if __name__ == "__main__":
    shell_cp(__file__   )
