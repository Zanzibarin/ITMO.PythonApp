# -*- coding: cp1251 -*-
print("������������ ������� 4. ���������� ���������� ��������� � ������ ")

from random import randint
import time


#���� ���� �������
igrok1 = input('������� ��� 1-�� ������: ')
igrok2 = input('������� ��� 2-�� ������: ')


#���������� �������� ����� � �����
wins_counter1 = 0
wins_counter2 = 0
sum_of_points1 = 0
sum_of_points2 = 0

for i in range(5):

    #������������� �������� ������ 1 �������
    print('')
    print('�����', i+1)
    print('����� �������', igrok1)
    time.sleep(1)
    n1 = randint (1, 6)
    print('������ �����', n1)
    sum_of_points1 += n1           # ��������� ����
    print('����� ����� ������', igrok1, '����� ������� �', i+1, '�����', sum_of_points1)

    # ������������� �������� ������ 2 �������
    print('����� �������', igrok2)
    time.sleep(1)
    n2 = randint (1, 6)
    print('������ �����', n2)
    sum_of_points2 += n2           # ��������� ����
    print('����� ����� ������', igrok2, '����� ������� �', i+1, '�����', sum_of_points2)

    if n1 > n2:
        wins_counter1 +=1
        print('� ���� ������ �������', igrok1)
    elif n1 < n2:
        wins_counter2 +=1
        print('� ���� ������ �������', igrok2)
    else:
        print('�����')
    

# ����������� ����������
if wins_counter1 > wins_counter2:
    print('')
    print('�������', igrok1)
    print('���������� �����', wins_counter1)
    print('����� �����', sum_of_points1)
elif wins_counter2 > wins_counter1:
    print('')
    print('�������', igrok2)
    print('���������� �����', wins_counter2)
    print('����� �����', sum_of_points2)
else:
    print('')
    print('�����')