# -*- coding: utf-8 -*-

import os
import shutil
import platform
import sys



def add_separators(f):
    # inner - итоговая функция с новым поведение
    def inner(*args, **kwargs):
        # поведение до вызова
        print()
        print('*' * 1000)
        result = f(*args, **kwargs)
        # поведение после вызова
        print('*' * 1000)
        print()
        return result

    # возвращается функция inner с новым поведением
    return inner

@add_separators
def folder():
    folder_name = input("Введите название папки: ")
    os.mkdir(f'{folder_name}')
    print('Создана папка: ', folder_name)

@add_separators
def folder_delete():
    folder_delete = input('Введите название папки, которую хотите удалить: ')
    os.rmdir(f'{folder_delete}') if os.path.exists(f'{folder_delete}') else print('Такой папки не существует')

@add_separators
def folder_folder_file_copy():
    name_folder_file = input('Введите название папки/файла: ')
    name_folder_file_copy = input('Введите название копии папки/файла: ')
    shutil.copytree(name_folder_file, name_folder_file_copy)

@add_separators
def contents_working_directory():
    print(os.listdir())


path = os.getcwd()
@add_separators
def viewing_folders():
    result = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
    print(result)

@add_separators
def viewing_files():
    result = [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]
    print(result)

@add_separators
def operating_system():
    print(sys.platform)
    print(platform.system())

@add_separators
def creator_program():
    print('Создатель программы:  Курочкин Александр Васильевич')

@add_separators
def invalid_menu_item():
    print('Неверный пункт меню')