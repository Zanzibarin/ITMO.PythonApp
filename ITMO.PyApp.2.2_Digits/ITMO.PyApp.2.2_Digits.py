# -*- coding: cp1251 -*-
print("������������ ������� 2. ������ � �������")
print("������ � �������")
print('')

print("----- ������ 02 -----")
a = int(16)
b = int(8)
c = int(a/b)
print("�������� ������� ������ ����� 16 �� 8")
print(c)

d = int(b/a)
print("�������� ������� ������ ����� 8 �� 16")
print(d)

e = int(b%a)
print("�������� ������ ������� ������ ����� 8 �� 16")
print(e)

f = int(a%b)
print("�������� ������ ������� ������ ����� 16 �� 8")
print(f)

g = int(a ** b)
print("�������� ���������� ����� 16 � ������� 8")
print(g)
print('')

print("----- ������ 03 -----")
#param = "string" + 15 ����� ������
#������� - �������������� � ������
param = "string" + str(15)
print(param)
print('')

print("----- ������ 04 -----")
print("�������� �������� �����")
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " + " + n2 + " = ", n3)
