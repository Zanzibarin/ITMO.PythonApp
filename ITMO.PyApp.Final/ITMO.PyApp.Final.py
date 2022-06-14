# -*- coding: cp1251 -*-
print('Ввод и вывод из массива статической последовательности известной длины')
print('')

var_list = []
i = 0

while i < 5:
    var_list.append(input('Вставте новый элемент в список: '))
    print('Список обновлён', var_list)
    i = i + 1

for i in range (1):
    print('Список заполнен!')