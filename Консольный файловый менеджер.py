import os
import platform
import shutil
import sys
from victory import victorina
from use_functions import accaunt
from directory import new_directory



while True:
    print('1. создать папку')
    print('2. удалить(файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в вмкторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. выход')

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
    elif choice == '5':
        name_list_isdir = []
        # print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))])
        for name in os.listdir(path):
            if os.path.isdir(os.path.join(path, name)):
                name_list_isdir.append(name)
        print(name_list_isdir)
    elif choice == '6':
        name_list_isfile = []
        # print([ name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name)) ])
        for name in os.listdir(path):
            if os.path.isfile(os.path.join(path, name)):
                name_list_isfile.append(name)
        print(name_list_isfile)
    elif choice == '7':
        print(sys.platform)
        print(platform.system())
    elif choice == '8':
        print('Создатель программы:  Курочкин Александр Васильевич')
    elif choice == '9':
        victorina()
    elif choice == '10':
        accaunt()
    elif choice == '11':
        new_directory()
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню') 