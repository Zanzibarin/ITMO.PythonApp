# -*- coding: cp1251 -*-
print("������������ ������� 2. ������ � �������")
print("�������")
print('')

print("----- ������ 03 / 04 -----")
seq = (8,8,23,97,92,44,17,39,11,12)
print(seq)
print(seq.count(8), ": seq.count ���������� ���������� ��������� � ��������� ���������")
print(seq.index(44), ": seq.index ���������� ���������� ������ �������� � ������������������")
print('')

print("----- ������ 05 / 06 -----")
listseq = list(seq)
print(listseq, "- �������������� ������� � ������")
print(type(listseq), "- ����� (���) ����� �������������� � ������ (list)")
print('')

print("----- ������ 07 -----")
print("�������� ������ �������� �������, ����������� � ������ ��� ���������������� ��������.")
listseq.sort(reverse=True)
print(listseq, "���������� reverse=True")
listseq.append(1000)
print(listseq, "append(1000)")
del listseq[-1]
print(listseq, "del list[-1] ")
listseq.pop(len(listseq)-1)
print(listseq, "pop(len(list) -1 ")
print('')