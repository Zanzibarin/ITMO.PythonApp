# -*- coding: cp1251 -*-
print("������������ ������� 2. ������ � �������")
print("������ �� ��������")
print('')

print("----- ������ 01 -----")
string1 = " This is a string. "
print(string1)
string2 = " This is another string. "
print(string2)
print('')

print("----- ������ 02 -----")
# ������ 2
a = string1 + string2
print(a)
print('')

# ������ 3
print("----- ������ 03 -----")
print(len(string1))
print(string1.title())
print(string1.lower())
print(string1.upper())
print(string1.rstrip())
print(string1.lstrip())
print(string1.strip())
print(string1.strip('0'))
print('')

print("----- ������ 04 -----")
d = "qwerty"
ch = d[2]
print(ch)
print('')

print("----- ������ 05 -----")
chm = d[1:3]
print(chm)
print('')

print("----- ������ 06 -----")
chm = d[1:]
print(chm)
chm = d[:3]
print(chm)
chm = d[:]
print(chm)
chm = d[1:5:2]
print(chm)

print("----- ������ 07 -----")
d[2] = 'o'
print(d)

