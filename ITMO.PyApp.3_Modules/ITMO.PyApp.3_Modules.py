# -*- coding: cp1251 -*-
print("Практическое занятие 3. Работа с модулями стандартной библиотеки")

import math
import statistics
import random

print("Вывод списка")
list_math = [82,8,23,97,92,44,17,39,11,12]
print(list_math)
print('')

print("Сумма всех чисел списка")
res_sum = math.fsum(list_math)
print(res_sum)
print('')

print("Среднее значение всех чисел списка")
res_mean = statistics.mean(list_math) 
print(res_mean)
print('')

print("Медианное значение всех чисел списка")
res_median = statistics.median(list_math) 
print(res_median)
print('')

print("Стандартное отклонение")
res_stdev = statistics.stdev(list_math) 
print(res_stdev)
print('')

print("Генерация случайного числа")
rnadom_int = random.randint(1, 100)
print(rnadom_int)
