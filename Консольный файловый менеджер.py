import os
import platform
import shutil
import sys
from victory import victorina
from My_bank_account import accaunt
from directory import new_directory



while True:
    print('1. ������� �����')
    print('2. �������(����/�����)')
    print('3. ���������� (����/�����)')
    print('4. �������� ����������� ������� ����������')
    print('5. ���������� ������ �����')
    print('6. ���������� ������ �����')
    print('7. �������� ���������� �� ������������ �������')
    print('8. ��������� ���������')
    print('9. ������ � ���������')
    print('10. ��� ���������� ����')
    print('11. ����� ������� ����������')
    print('12. �����')

    path = os.getcwd()
    choice = input('�������� ����� ����: ')
    if choice == '1':
        folder_name = input('������� �������� �����: ')
        os.mkdir(f'{folder_name}')
        print('������� �����: ', folder_name)
    elif choice == '2':
        folder_delete = input('������� �������� �����, ������� ������ �������: ')
        if os.path.exists(f'{folder_delete}'):
            os.rmdir(f'{folder_delete}')
            print('������� �����: ', folder_delete)
        else:
            print('�������� ����� ����')
            print('����� ����� �� ����������')
    elif choice == '3':
        name_folder_file = input('������� �������� �����/�����: ')
        name_folder_file_copy = input('������� �������� ����� �����/�����: ')
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
        print('��������� ���������:  �������� ��������� ����������')
    elif choice == '9':
        victorina()
    elif choice == '10':
        accaunt()
    elif choice == '11':
        new_directory()
    elif choice == '12':
        break
    else:
        print('�������� ����� ����')