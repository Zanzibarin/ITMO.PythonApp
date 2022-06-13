# -*- coding: cp1251 -*-
print("Практическое занятие 2. Работа с данными")
print("КОРТЕЖИ")
print('')

print("----- Задача 03 / 04 -----")
seq = (8,8,23,97,92,44,17,39,11,12)
print(seq)
print(seq.count(8), ": seq.count возвращает количество элементов с указанным значением")
print(seq.index(44), ": seq.index возвращает порядковый индекс элемента в последовательности")
print('')

print("----- Задача 05 / 06 -----")
listseq = list(seq)
print(listseq, "- Преобразование кортежа в список")
print(type(listseq), "- Класс (тип) после преобразования в список (list)")
print('')

print("----- Задача 07 -----")
print("Проверка работы основных методов, применяемых к списку для преобразованного «кортежа».")
listseq.sort(reverse=True)
print(listseq, "сортировка reverse=True")
listseq.append(1000)
print(listseq, "append(1000)")
del listseq[-1]
print(listseq, "del list[-1] ")
listseq.pop(len(listseq)-1)
print(listseq, "pop(len(list) -1 ")
print('')