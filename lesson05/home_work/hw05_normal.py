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

import os
import sys
import shutil
import hw05_easy as easy

print('sys.argv = ', sys.argv)


def print_help():
    print('help - получение справки')
    print("change_dir <path> - перемещение в указанную директорию")
    print('list_dir - отображение папок находящихся в текущей директории')
    print('del_folder <path>  - удаление директории по указанному пути')
    print('make_folder <path>  - создание директории по указанному пути')



do = {
    "help": print_help,
    "make_folder": easy.make_folder,
    "del_folder": easy.del_folder,
    "list_dir": easy.list_dir,
    "change_dir": easy.change_dir
    }


try:
    stringpath = sys.argv[2]
except IndexError:
    stringpath = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
