# -*- coding: cp1251 -*-
print("������������ ������� 2. ������ � �������")
print("������ �� ��������")
print('')

print("----- ������ 01 -----")
list1 = [82,8,23,97,92,44,17,39,11,12]
print(list1)
print('')

print("----- ������ 04 -----")
list1[4] = 500
print(list1)
print('')

print("----- ������ 05 -----")
list1.append(100)
print(list1)
print('')

print("----- ������ 06 -----")
list1.insert(2, 1000)
print(list1)
print('')

print("----- ������ 07 -----")
list1.pop(0)
print(list1)
print('')

print("----- ������ 08 -----")
list1.pop(len(list1)-1)
print(list1)
print('')

print("-----------------------------------------------------------------------")
print("���������� ��������� ������")
print('')

print("----- ������ 01 / 02-----")
print(list1, "������ ��� ����������")
list1.sort(reverse=True)
print(list1, "������ � ����������� �� ��������")
print(sorted(list1), "������ � ����������� �� �����������")
print('')

print("----- ������ 03 / 04 -----")
list2 = [3,5,6,2,33,6,11]
lis = sorted(list2)
print(lis)