import random
# �������� ������� ��������� ������� - ���� ��������
def victorina():
    dict_people_data = {'������ ������':'04.01.1965',
                        '������� ���������': '06.01.1938',
                        '�������� �����': '07.01.1964',
                        '������ ����': '08.01.1947',
                        '������ ������': '08.01.1935',
                        '������� ����������� ��������': '10.01.1883',
                        '������� ���������': '14.01.1948',
                        '��������� ���������': '25.01.1938',
                        '������ ��������� ������': '29.01.1860',
                        '���� ���������': '31.01.1981'}
    # ��������� ���������� �������� ������ ������� dict_people_data
    people_Ormond_data = dict_people_data['������ ������']
    people_Chelentano_data = dict_people_data['������� ���������']
    people_Keydj_data = dict_people_data['�������� �����']
    people_Boui_data = dict_people_data['������ ����']
    people_Presli_data = dict_people_data['������ ������']
    people_Tolstoy_data = dict_people_data['������� ����������� ��������']
    people_Harlamov_data = dict_people_data['������� ���������']
    people_Wisockiy_data = dict_people_data['��������� ���������']
    people_Chehov_data = dict_people_data['������ ��������� ������']
    people_Nachalova_data = dict_people_data['���� ���������']

    # ������� ������ �� ��������� �����
    people_list = ['������ ������', '������� ���������', '�������� �����', '������ ����', '������ ������', '������� ����������� ��������', '������� ���������',
                 '��������� ���������', '������ ��������� ������', '���� ���������']
    # ������� ������ ��� �������� ���������� �������
    correct_answer = []
    # ������� ������ ��� �������� ������������ �������
    no_correct_answer = []
    # ������� ��������� ���������� ��������� ����� ��� ������ ���������
    result_dict_people_data = random.sample(dict_people_data.keys(), 5)
    print(result_dict_people_data)
    # �������� ����� ������� �������� ���� �� ������ ���� �������� ���� ��������� �����
    for i in result_dict_people_data:
        people = input('������� ���� �������� ' + i + ': ')
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
            # �������� ������ ���������� �������
            if i in people_list[0]:
                print('��������� ������ 1965 ����')
            elif i in people_list[1]:
                print('������ ������ 1938 ����')
            elif i in people_list[2]:
                print('������� ������ 1964 ����')
            elif i in people_list[3]:
                print('������� ������ 1947 ����')
            elif i in people_list[4]:
                print('������� ������ 1935 ����')
            elif i in people_list[5]:
                print('������� ������ 1883 ����')
            elif i in people_list[6]:
                print('������������� ������ 1948 ����')
            elif i in people_list[7]:
                print('�������� ����� ������ 1938 ����')
            elif i in people_list[8]:
                print('�������� ������� ������ 1860 ����')
            elif i in people_list[9]:
                print('�������� ������ ������ 1981 ����')
    # ����� ���������� ���������� �������
    print('���������� ������ �������: ', len(correct_answer))
    # ����� ���������� �� ���������� �������
    print('���������� �������� �������: ', len(no_correct_answer))
    # ����������� ������ ������
    print('�������� ������� !!')
    return None