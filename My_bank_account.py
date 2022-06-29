def accaunt():
    score = 0
    purchase = []
    summa_purchase_dict = {}
    purchase_dict = {}
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            summa = float(input('Введите сумму пополнения счёта: '))
            score += summa
            pass
        elif choice == '2':
            summa_purchase = float(input('Введите сумму покупки: '))
            if summa_purchase > score:
                print('Денег не хватает')
            elif summa_purchase <= score:
                purchase_name = input('Введите название покупки: ')
                withdraw_moneu_from_the_score = score - summa_purchase
                purchase.append(purchase_name)
                purchase_dict['Название покупки'] = purchase_name
                summa_purchase_dict['Сумма покупки'] = summa_purchase
            pass
        elif choice == '3':
            print(purchase_dict)
            print(summa_purchase_dict)
            pass
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

accaunt()