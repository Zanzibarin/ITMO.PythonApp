print("Practice 2. Data processing")
print("Lists")
print('')

print("----- Task 01 -----")
list1 = [82,8,23,97,92,44,17,39,11,12]
print(list1)
print('')

print("----- Task 04 -----")
list1[4] = 500
print(list1)
print('')

print("----- Task 05 -----")
list1.append(100)
print(list1)
print('')

print("----- Task 06 -----")
list1.insert(2, 1000)
print(list1)
print('')

print("----- Task 07 -----")
list1.pop(0)
print(list1)
print('')

print("----- Task 08 -----")
list1.pop(len(list1)-1)
print(list1)
print('')

print("-----------------------------------------------------------------------")
print("List sorting")
print('')

print("----- Task 01 / 02-----")
print(list1, "Unsorted list")
list1.sort(reverse=True)
print(list1, "Decremental sorting")
print(sorted(list1), "Incremental sorting")
print('')

print("----- Task 03 / 04 -----")
list2 = [3,5,6,2,33,6,11]
lis = sorted(list2)
print(lis)