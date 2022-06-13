# -*- coding: cp1251 -*-
print("Практическое занятие 2. Работа с данными")
print("РАБОТА СО СТРОКАМИ")
print('')

print("----- Задача 01 -----")
string1 = " This is a string. "
print(string1)
string2 = " This is another string. "
print(string2)
print('')

print("----- Задача 02 -----")
# Задача 2
a = string1 + string2
print(a)
print('')

# Задача 3
print("----- Задача 03 -----")
print(len(string1))
print(string1.title())
print(string1.lower())
print(string1.upper())
print(string1.rstrip())
print(string1.lstrip())
print(string1.strip())
print(string1.strip('0'))
print('')

print("----- Задача 04 -----")
d = "qwerty"
ch = d[2]
print(ch)
print('')

print("----- Задача 05 -----")
chm = d[1:3]
print(chm)
print('')

print("----- Задача 06 -----")
chm = d[1:]
print(chm)
chm = d[:3]
print(chm)
chm = d[:]
print(chm)
chm = d[1:5:2]
print(chm)

print("----- Задача 07 -----")
d[2] = 'o'
print(d)

