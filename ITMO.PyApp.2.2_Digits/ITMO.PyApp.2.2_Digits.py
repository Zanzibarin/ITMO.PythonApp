# -*- coding: cp1251 -*-
print("Практическое занятие 2. Работа с данными")
print("РАБОТА С ЧИСЛАМИ")
print('')

print("----- Задача 02 -----")
a = int(16)
b = int(8)
c = int(a/b)
print("Операция деления целого числа 16 на 8")
print(c)

d = int(b/a)
print("Операция деления целого числа 8 на 16")
print(d)

e = int(b%a)
print("Операция взятия остатка целого числа 8 от 16")
print(e)

f = int(a%b)
print("Операция взятия остатка целого числа 16 от 8")
print(f)

g = int(a ** b)
print("Операция возведения числа 16 в степень 8")
print(g)
print('')

print("----- Задача 03 -----")
#param = "string" + 15 Будет ошибка
#Решение - преобразование к строке
param = "string" + str(15)
print(param)
print('')

print("----- Задача 04 -----")
print("Сложение вводимых чисел")
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " + " + n2 + " = ", n3)
