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
    score = []                             # список куда сохраняется сумма пополняемого счета
    purchase_list = []
    purchases_dict = {}

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            summa = float(input('Введите сумму пополнения счёта: '))
            score.append(summa)
            with open('score.txt', 'a') as f:
                f.write(f'{sum(score)}\n')        # запись в файл суммы счета
        elif choice == '2':
            summa_purchase = float(input('Введите сумму покупки: '))
            if summa_purchase > sum(score):
                    print('Денег не хватает')
            elif summa_purchase <= sum(score):
                purchase_name = input('Введите название покупки: ')
                purchase_list.append(purchase_name)
                # purchases_dict[purchase_name] = summa_purchase
        elif choice == '3':
            with open('purchase_history.txt', 'a') as f:
                for purchases in purchase_list:
                    purchases_dict[purchases] = summa_purchase
                f.write(f'{purchases_dict}\n')
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

accaunt()