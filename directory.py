import os

def new_directory():
    os.chdir(input('Ведите директорию для изменения: '))
    print('os.getcwd :', os.getcwd())

