# -*- coding: cp1251 -*-
print("Практическое занятие 2. Работа с данными")
print("РАБОТА СО СПИСКАМИ")
print('')

print("----- Задача 01 -----")
list1 = [82,8,23,97,92,44,17,39,11,12]
print(list1)
print('')

print("----- Задача 04 -----")
list1[4] = 500
print(list1)
print('')

print("----- Задача 05 -----")
list1.append(100)
print(list1)
print('')

print("----- Задача 06 -----")
list1.insert(2, 1000)
print(list1)
print('')

print("----- Задача 07 -----")
list1.pop(0)
print(list1)
print('')

print("----- Задача 08 -----")
list1.pop(len(list1)-1)
print(list1)
print('')

print("-----------------------------------------------------------------------")
print("Сортировка элементов списка")
print('')

print("----- Задача 01 / 02-----")
print(list1, "Список без сортировки")
list1.sort(reverse=True)
print(list1, "Список с сортировкой по убыванию")
print(sorted(list1), "Список с сортировкой по возрастанию")
print('')

print("----- Задача 03 / 04 -----")
list2 = [3,5,6,2,33,6,11]
lis = sorted(list2)
print(lis)