# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os
import shutil
import sys


# 'make_folders <path>  - создание 9-ти директорий по указанному пути'
def make_folders():
    if not stringpath:
        print("Необходимо указать имя директории вторым параметром")
        return
    for i in range(1, 10):
        dir_path = os.path.join(os.getcwd(), stringpath + str(i))
        try:
            os.makedirs(dir_path)
        except OSError:
            print(f"Ошибка. Директория {dir_path} не создана")
        else:
            print(f"Директория {dir_path} создана")


# 'del_folders <path>  - удаление созданых командой make_folders 9-ти директорий по указанному пути'
def del_folders():
    if not stringpath:
        print("Необходимо указать имя директории вторым параметром")
        return
    for i in range(1, 10):
        dir_path = os.path.join(os.getcwd(), stringpath + str(i))
        try:
            os.rmdir(dir_path)
        except OSError:
            print(f"Ошибка. Директория {dir_path} не удалена")
        else:
            print(f"Директория {dir_path} удалена")


# 'make_folder <path>  - создание директории по указанному пути'
def make_folder():
    if not stringpath:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), stringpath)
    try:
        os.makedirs(dir_path)
    except OSError:
        print(f"Ошибка. Директория {dir_path} не создана")
    else:
        print(f"Директория {dir_path} создана")


# 'del_folder <path>  - удаление директории по указанному пути'
def del_folder():
    if not stringpath:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), stringpath + str(i))
    try:
        os.rmdir(dir_path)
    except OSError:
        print(f"Ошибка. Директория {dir_path} не удалена")
    else:
        print(f"Директория {dir_path} удалена")


# 'list_dir - отображение папок находящихся в текущей директории'
def list_dir():
    print(os.listdir(os.getcwd()))


# 'copy_file' копирование исполняемого файла
def copy_file():
    file_name = os.path.basename(__file__)
    shutil.copyfile(file_name, os.path.dirname(file_name) + "copy_" + os.path.basename(file_name))
    print(f"Файл {os.path.basename(file_name)} скопирован")


# 'change_dir' перемещение в указанную директорию
def change_dir():
    if not stringpath:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), stringpath)
    try:
        os.chdir(dir_path)
    except OSError:
        print(f"Ошибка. Директория {dir_path} не найдена")
    else:
        print(f"Вы переместились в директорию {dir_path}")


try:
    stringpath = sys.argv[2]
except IndexError:
    stringpath = None
    
