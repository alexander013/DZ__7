import simplejson as json

# -*- coding: utf-8 -*-
"""
схраннение названия плкупки и цены
"""
# import os
# import pickle
#
# FILE_NAME = 'orders_pickle.data'
#
# orders = []
# print(orders)
# if os.path.exists(FILE_NAME):
#     with open(FILE_NAME, 'rb') as f:
#         orders = pickle.load(f)
#         print(orders)
#
#
#
#
# name = input('Введите название покупки: ')
# cost = int(input('Введите цену: '))
# order = (name, cost)
# orders.append(order)
#
# with open(FILE_NAME, 'wb') as f:
#     pickle.dump(orders, f)

person = {'llll': 3000.0,
          'fffff': 45466}

print(' В формате json')
print(type(person))
result = json.dumps(person)
print(result)
print(type(result))

print(' В исходном формате')
person_recovery = json.loads(result)
print(person_recovery)
print(type(person_recovery))

print(person == person_recovery)


# сохранение в файл
with open('person.json', 'w') as f:
    json.dump(person, f)

with open('person.json', 'r') as f:
    json.load(f)