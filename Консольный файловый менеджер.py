# -*- coding: utf-8 -*-

import os
import platform
import shutil
import sys
from victory import victorina
from My_bank_account import accaunt
from directory import new_directory

name_list_isdir = []
name_list_isfile = []

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
    print('Создана папка: ', folder_name)


while True:
    print('1. создать папку')
    print('2. удалить(файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. сохранить содержимое рабочей директории в файл')
    print('8. просмотр информации об операционной системе')
    print('9. создатель программы')
    print('10. играть в вмкторину')
    print('11. мой банковский счет')
    print('12. смена рабочей директории')
    print('13. выход')

    path = os.getcwd()
    choice = input('Выберите пункт меню: ')

    if choice == '1':
        folder_name = input("Введите название папки: ")
        os.mkdir(f'{folder_name}')
        # print('Создана папка: ', folder_name)
        folder()
    elif choice == '2':
        folder_delete = input('Введите название папки, которую хотите удалить: ')
        # if os.path.exists(f'{folder_delete}'):      # проверка на существование файла, который хотите удалить с помощью метода os.path.exists
        #     os.rmdir(f'{folder_delete}')
        #     print('Удалена папка: ', folder_delete)
        # else:
        #     print('Такой папки не существует')


        print('Удалена папка: ', folder_delete) and os.rmdir(f'{folder_delete}') if os.path.exists(f'{folder_delete}') else print('Такой папки не существует')



    elif choice == '3':
        name_folder_file = input('Введите название папки/файла: ')
        name_folder_file_copy = input('Введите название копии папки/файла: ')
        shutil.copytree(name_folder_file, name_folder_file_copy)
    elif choice == '4':
        print(os.listdir())
    elif choice == '5':         # просмотр только папок
    #     for name in os.listdir(path):
    #         if os.path.isdir(os.path.join(path, name)):
    #             name_list_isdir.append(name)
    #     print(name_list_isdir)
        result = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
        print(result)
    elif choice == '6':         # просмотр только файлов
        # for name in os.listdir(path):
        #     if os.path.isfile(os.path.join(path, name)):
        #         name_list_isfile.append(name)
        # print(name_list_isfile)
        result = [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]
        print(result)
    elif choice == '7':               # сохранить содержимое рабочей директории в файл
        # for name in os.listdir(path):
        #     if os.path.isfile(os.path.join(path, name)):
        #         name_list_isfile.append(name)
        result_isfile = [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]
        print(result_isfile)
        with open('listdir.txt', 'w') as f:
            f.write(f'files: ')
            f.write(f'{result_isfile}\n')
        # for name in os.listdir(path):
        #     if os.path.isdir(os.path.join(path, name)):
        #         name_list_isdir.append(name)
        result_isdir = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
        with open('listdir.txt', 'a') as f:
            f.write(f'dirs: ')
            f.write(f'{result_isdir}\n')
    elif choice == '8':
        print(sys.platform)
        print(platform.system())
    elif choice == '9':
        print('Создатель программы:  Курочкин Александр Васильевич')
    elif choice == '10':
        victorina()
    elif choice == '11':
        accaunt()
    elif choice == '12':
        new_directory()
    elif choice == '13':
        break
    else:
        print('Неверный пункт меню')