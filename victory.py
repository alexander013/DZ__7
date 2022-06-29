import random
# Создание словаря известный человек - дата рождения
def victorina():
    dict_people_data = {'Джулии Ормонд':'04.01.1965',
                        'Адриано Челентано': '06.01.1938',
                        'Николаса Кейдж': '07.01.1964',
                        'Дэвида Боуи': '08.01.1947',
                        'Элвиса Прэсли': '08.01.1935',
                        'Алексея Николаевича Толстого': '10.01.1883',
                        'Валерия Харламова': '14.01.1948',
                        'Владимира Высоцкого': '25.01.1938',
                        'Антона Павловича Чехова': '29.01.1860',
                        'Юлии Началовой': '31.01.1981'}
    # Приисваем переменным значения ключей словаря dict_people_data
    people_Ormond_data = dict_people_data['Джулии Ормонд']
    people_Chelentano_data = dict_people_data['Адриано Челентано']
    people_Keydj_data = dict_people_data['Николаса Кейдж']
    people_Boui_data = dict_people_data['Дэвида Боуи']
    people_Presli_data = dict_people_data['Элвиса Прэсли']
    people_Tolstoy_data = dict_people_data['Алексея Николаевича Толстого']
    people_Harlamov_data = dict_people_data['Валерия Харламова']
    people_Wisockiy_data = dict_people_data['Владимира Высоцкого']
    people_Chehov_data = dict_people_data['Антона Павловича Чехова']
    people_Nachalova_data = dict_people_data['Юлии Началовой']

    # Создаем список из известных людей
    people_list = ['Джулии Ормонд', 'Адриано Челентано', 'Николаса Кейдж', 'Дэвида Боуи', 'Элвиса Прэсли', 'Алексея Николаевича Толстого', 'Валерия Харламова',
                 'Владимира Высоцкого', 'Антона Павловича Чехова', 'Юлии Началовой']
    # Создаем список для хранения правильных ответов
    correct_answer = []
    # Создаем список для хранения неправильных ответов
    no_correct_answer = []
    # создаем случайное количество известных людей для начала викторины
    result_dict_people_data = random.sample(dict_people_data.keys(), 5)
    print(result_dict_people_data)
    # создание цикла который работает пока не введут даты рождения пяти известных людей
    for i in result_dict_people_data:
        people = input('Введите дату рождения ' + i + ': ')
        if people == people_Boui_data:
            correct_answer.append(people)
        elif people == people_Ormond_data:
            correct_answer.append(people)
        elif people == people_Chelentano_data:
            correct_answer.append(people)
        elif people == people_Keydj_data:
            correct_answer.append(people)
        elif people == people_Presli_data:
            correct_answer.append(people)
        elif people == people_Tolstoy_data:
            correct_answer.append(people)
        elif people == people_Harlamov_data:
            correct_answer.append(people)
        elif people == people_Wisockiy_data:
            correct_answer.append(people)
        elif people == people_Chehov_data:
            correct_answer.append(people)
        elif people == people_Nachalova_data:
            correct_answer.append(people)
        else:
            no_correct_answer.append(people)
            # Создание вывода правильных ответов
            if i in people_list[0]:
                print('четвертое января 1965 года')
            elif i in people_list[1]:
                print('шестое января 1938 года')
            elif i in people_list[2]:
                print('седьмое января 1964 года')
            elif i in people_list[3]:
                print('восьмое января 1947 года')
            elif i in people_list[4]:
                print('восьмое января 1935 года')
            elif i in people_list[5]:
                print('десятое января 1883 года')
            elif i in people_list[6]:
                print('четырнадцатое января 1948 года')
            elif i in people_list[7]:
                print('двадцать пятое января 1938 года')
            elif i in people_list[8]:
                print('двадцать девятое января 1860 года')
            elif i in people_list[9]:
                print('тридцать первое января 1981 года')
    # Вывод количества правильных ответов
    print('Количество верных ответов: ', len(correct_answer))
    # Вывод количества не правильных ответов
    print('Количество неверных ответов: ', len(no_correct_answer))
    # Предложение начать заново
    print('Начинаем сначала !!')
    return None