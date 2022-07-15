# -*- coding: utf-8 -*-

import os
import platform
import shutil
import sys
from victory import victorina
from My_bank_account import accaunt
from directory import new_directory
from Decorator import folder
from Decorator import folder_delete
from Decorator import folder_folder_file_copy
from Decorator import contents_working_directory
from Decorator import viewing_folders
from Decorator import viewing_files
from Decorator import operating_system
from Decorator import creator_program
from Decorator import invalid_menu_item

name_list_isdir = []
name_list_isfile = []

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
        folder()
    elif choice == '2':
        folder_delete()
    elif choice == '3':
        folder_folder_file_copy()
    elif choice == '4':
        contents_working_directory()            # просмотр содержимого рабочей директории с помощью метода os.listdir()
    elif choice == '5':                         # просмотр только папок
        viewing_folders()
    elif choice == '6':                         # просмотр только файлов
        viewing_files()
    elif choice == '7':                         # сохранить содержимое рабочей директории в файл
        result_isfile = [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]
        print(result_isfile)
        with open('listdir.txt', 'w') as f:
            f.write(f'files: ')
            f.write(f'{result_isfile}\n')
        result_isdir = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
        with open('listdir.txt', 'a') as f:
            f.write(f'dirs: ')
            f.write(f'{result_isdir}\n')
    elif choice == '8':
        operating_system()
    elif choice == '9':
        creator_program()
    elif choice == '10':
        victorina()
    elif choice == '11':
        accaunt()
    elif choice == '12':
        new_directory()
    elif choice == '13':
        break
    else:
        invalid_menu_item()