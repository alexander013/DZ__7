import os

def new_directory():
    os.chdir(input('������ ���������� ��� ���������: '))
    print('os.getcwd :', os.getcwd())

