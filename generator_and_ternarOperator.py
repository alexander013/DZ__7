# -*- coding: utf-8 -*-
import os

#
# # choice = input('Выберите пункт меню: ')
#
# # if choice == '1':
# #     folder_name = input('Введите название папки: ')
# #     os.mkdir(f'{folder_name}')
# #     print('Создана папка: ', folder_name)
#
# # Использование генератора
#
# # numbers = [1, 4, 2, 6, 7, 10, 100]
# # result = [number for number in numbers if number > 5 and number < 50]
# # print(result)
#
# # Использование тернарных операторов
# # print('13 в нашем списке') if 13 in numbers else print('Нет несчастливого числа')
# # result = 'Есть китайское несчастливое число' if 4 in numbers else 'Все ок'
# # os.mkdir(f'{input("Введите название папки: ")}') if choice == '1' else print('Неверный пункт меню')
# # print('Создана папка: ', folder_name)
#
# # Удаление файла с помощью тетрнарных операторов
#
# folder_delete = input('Введите название папки, которую хотите удалить: ')
# # if os.path.exists(f'{folder_delete}'):      # проверка на существование файла, который хотите удалить с помощью метода os.path.exists
# #     os.rmdir(f'{folder_delete}')
# #     print('Удалена папка: ', folder_delete)
# # else:
# #     print('Такой папки не существует')
# #
# # os.rmdir(f'{folder_delete}') if os.path.exists(f'{folder_delete}') else print('Такой папки не существует')
#
# print('Удалена папка: ', folder_delete) and os.rmdir(f'{folder_delete}' ) if os.path.exists(f'{folder_delete}') else print('Такой папки не существует')
#
#
# # # генератор списка
# # # [элемент <цикл for> if <условие>]
# #
# # result = [number for number in numbers if number > 5 and number < 50]
# # # print(result)
#
#
#
#
# name_list_isdir = []
# name_list_isfile = []
# path = os.getcwd()
#
#
# # for name in os.listdir(path):
# #     if os.path.isdir(os.path.join(path, name)):
# #         name_list_isdir.append(name)
# # print(name_list_isdir)
#
# result = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
# print(result)
#
# with open(FILE_NAME, 'r') as f:
#     for history in f:
#         print(str(history).replace("{", "").replace("}", "") for)
#
# if summa_purchase > score:
#     print('Денег не хватает')

def add_separators(f):
    # inner - итоговая функция с новым поведение
    def inner(*args, **kwargs):
        # поведение до вызова
        print('*' * 100)
        result = f(*args, **kwargs)
        # поведение после вызова
        print('*' * 100)
        return result

    # возвращается функция inner с новым поведением
    return inner




folder_name = input("Введите название папки: ")
os.mkdir(f'{folder_name}')

@add_separators
def folder():
    print('Создана папка: ', folder_name)

folder()
