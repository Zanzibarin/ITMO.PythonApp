# -*- coding: cp1251 -*-
print("Practice 2. Data processing")
print("Dictionaries")
print('')

print("----- Task 01 / 02 -----")
D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
print(D['food'])
print(D['quantity'] + 10)
print(D['color'])
print('')

print("----- Task 03 -----")
dp = {}
print(dp, " - Empty dictionary")
name = str(input("Input name: "))
age = int(input("Input age: "))
dp[name] = age
name = str(input("Input name: "))
age = int(input("Input age: "))
dp[name] = age
name = str(input("Input name: "))
age = int(input("Input age: "))
dp[name] = age
print(dp, " - Cmpleted dictionary")
print('')