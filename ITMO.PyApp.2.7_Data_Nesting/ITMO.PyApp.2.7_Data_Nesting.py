# -*- coding: cp1251 -*-
print("������������ ������� 2. ������ � �������")
print("����������� �������� ������")
print('')

'''
����������� ������� ��������� ������������� ������ � ����� �������, ���������� ��� � �������, ��������� �������� ����������, ���������� ������������, � ����� �������.
'''

rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'}, 'job': ['dev', 'mgr'], 'age': 25}

print(rec['name']['firstname'], rec['name']['lastname'], " - ��� � �������")
print(rec['name']['firstname'], " - ������ ���")
rec['job'].append('janitor'), #���������� ����� ���������
print(rec['job'], " - ���������� ������ ���������� � ���������� janitor")
print('')

print(rec['name']['firstname'], rec['name']['lastname'], rec['job'], rec['age'])