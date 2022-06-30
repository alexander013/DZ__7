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

while True:
    print('1. создать папку')
    print('2. удалить(файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. оохранить содержимое рабочей директории в файл')
    print('8. просмотр информации об операционной системе')
    print('9. создатель программы')
    print('10. играть в вмкторину')
    print('11. мой банковский счет')
    print('12. смена рабочей директории')
    print('13. выход')

    path = os.getcwd()
    choice = input('Выберите пункт меню: ')
    if choice == '1':
        folder_name = input('Введите название папки: ')
        os.mkdir(f'{folder_name}')
        print('Создана папка: ', folder_name)
    elif choice == '2':
        folder_delete = input('Введите название папки, которую хотите удалить: ')
        if os.path.exists(f'{folder_delete}'):
            os.rmdir(f'{folder_delete}')
            print('Удалена папка: ', folder_delete)
        else:
            print('Неверный пункт меню')
            print('Такой папки не существует')
    elif choice == '3':
        name_folder_file = input('Введите название папки/файла: ')
        name_folder_file_copy = input('Введите название копии папки/файла: ')
        shutil.copytree(name_folder_file, name_folder_file_copy)
    elif choice == '4':
        print(os.listdir())
    elif choice == '5':         # просмотр только папок
        for name in os.listdir(path):
            if os.path.isdir(os.path.join(path, name)):
                name_list_isdir.append(name)
        print(name_list_isdir)
    elif choice == '6':         # просмотр только файлов
        for name in os.listdir(path):
            if os.path.isfile(os.path.join(path, name)):
                name_list_isfile.append(name)
        print(name_list_isfile)
    elif choice == '7':
        for name in os.listdir(path):
            if os.path.isfile(os.path.join(path, name)):
                name_list_isfile.append(name)
        with open('listdir.txt', 'w') as f:
            f.write(f'files: ')
            f.write(f'{name_list_isfile}\n')
        for name in os.listdir(path):
            if os.path.isdir(os.path.join(path, name)):
                name_list_isdir.append(name)
        with open('listdir.txt', 'a') as f:
            f.write(f'dirs: ')
            f.write(f'{name_list_isdir}\n')
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