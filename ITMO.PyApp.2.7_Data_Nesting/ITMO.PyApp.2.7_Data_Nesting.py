# -*- coding: cp1251 -*-
print("Практическое занятие 2. Работа с данными")
print("ВЛОЖЕННОСТЬ ХРАНЕНИЯ ДАННЫХ")
print('')

'''
Реализовать сложную структуру представления данных о некой персоне, включающая имя и фамилию, несколько названий должностей, занимаемых одновременно, а также возраст.
'''

rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'}, 'job': ['dev', 'mgr'], 'age': 25}

print(rec['name']['firstname'], rec['name']['lastname'], " - Имя и фамилия")
print(rec['name']['firstname'], " - Только имя")
rec['job'].append('janitor'), #Добавление новой должности
print(rec['job'], " - Обновлённый список должностей с должностью janitor")
print('')

print(rec['name']['firstname'], rec['name']['lastname'], rec['job'], rec['age'])