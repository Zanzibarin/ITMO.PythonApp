# -*- coding: cp1251 -*-
print("������������ ������� 3. ������ � �������� ����������� ����������")

import math
import statistics
import random

print("����� ������")
list_math = [82,8,23,97,92,44,17,39,11,12]
print(list_math)
print('')

print("����� ���� ����� ������")
res_sum = math.fsum(list_math)
print(res_sum)
print('')

print("������� �������� ���� ����� ������")
res_mean = statistics.mean(list_math) 
print(res_mean)
print('')

print("��������� �������� ���� ����� ������")
res_median = statistics.median(list_math) 
print(res_median)
print('')

print("����������� ����������")
res_stdev = statistics.stdev(list_math) 
print(res_stdev)
print('')

print("��������� ���������� �����")
rnadom_int = random.randint(1, 100)
print(rnadom_int)
