import os
import json
import simplejson as json

# ЗАДАНИЕ 1
# 1. В подпрограмме Мой банковский счет;
# 2. Добавить сохранение суммы счета в файл.
#
# При первом открытии программы на счету 0
# После того как мы воспользовались программой и вышли сохранить сумму счета
# При следующем открытии программы прочитать сумму счета, которую сохранили

# 3. Добавить сохранение истории покупок в файл
# При первом открытии программы истории нет.
# После того как мы что нибудь купили и закрыли программу сохранить историю покупок.
# При следующем открытии программы прочитать историю и новые покупки уже добавлять к ней;

def accaunt():

    score = 0

    FILE_NAME = 'purchase_history.txt'

    purchases_dict = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            for history in f:
                print(str(history).replace("{", "").replace("}", ""))

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            summa = float(input('Введите сумму пополнения счёта: '))
            score = score + summa
            with open('score.txt', 'a') as f:
                f.write(f'Текущий личный счёт: ')
                f.write(f'{score}\n')        # запись в ЛИЧНОГО счета
        elif choice == '2':
            summa_purchase = float(input('Введите сумму покупки: '))
            if summa_purchase > score:
                    print('Денег не хватает')
            elif summa_purchase <= score:
                score = score - summa_purchase
                with open('score.txt', 'a') as f:
                    f.write(f'Остаток личного счёта: ')
                    f.write(f'{score}\n')
                purchase_name = input('Введите название покупки: ')
                purchases_dict[purchase_name] = summa_purchase
                result = json.dumps(purchases_dict)
        elif choice == '3':
            with open(FILE_NAME, 'a') as f:
                f.write(f'Покупки: ')
                f.write(f'{purchases_dict}\n')
            print(purchases_dict)
            with open('purchase_history.json', 'w') as f:
                json.dump(purchases_dict, f)

        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

accaunt()