# -*- coding: cp1251 -*-
print("������������ ������� 2. ������ � �������")
print("�������")
print('')

print("----- ������ 01 / 02 -----")
D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
print(D['food'])
print(D['quantity'] + 10)
print(D['color'])
print('')

print("----- ������ 03 -----")
dp = {}
print(dp, " - ������ �������")
name = str(input("������� ���: "))
age = int(input("������� �������: "))
dp[name] = age
name = str(input("������� ���: "))
age = int(input("������� �������: "))
dp[name] = age
name = str(input("������� ���: "))
age = int(input("������� �������: "))
dp[name] = age
print(dp, " - ����������� �������")
print('')