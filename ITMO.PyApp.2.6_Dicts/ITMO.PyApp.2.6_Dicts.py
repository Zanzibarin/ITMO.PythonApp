# -*- coding: cp1251 -*-
print("Практическое занятие 2. Работа с данными")
print("СЛОВАРИ")
print('')

print("----- Задача 01 / 02 -----")
D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
print(D['food'])
print(D['quantity'] + 10)
print(D['color'])
print('')

print("----- Задача 03 -----")
dp = {}
print(dp, " - Пустой словарь")
name = str(input("Введите имя: "))
age = int(input("Введите возраст: "))
dp[name] = age
name = str(input("Введите имя: "))
age = int(input("Введите возраст: "))
dp[name] = age
name = str(input("Введите имя: "))
age = int(input("Введите возраст: "))
dp[name] = age
print(dp, " - Заполненный словарь")
print('')