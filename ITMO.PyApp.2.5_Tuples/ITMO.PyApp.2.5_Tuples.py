print("Practice 2. Data processing")
print("Tuples")
print('')

print("----- Task 03 / 04 -----")
seq = (8,8,23,97,92,44,17,39,11,12)
print(seq)
print(seq.count(8), )
print(seq.index(44), )
print('')

print("----- Task 05 / 06 -----")
listseq = list(seq)
print(listseq, "- Converting tuple into list")
print(type(listseq), "- Class (type) after converting (list)")
print('')

print("----- Task 07 -----")
listseq.sort(reverse=True)
print(listseq, "sorting reverse=True")
listseq.append(1000)
print(listseq, "append(1000)")
del listseq[-1]
print(listseq, "del list[-1] ")
listseq.pop(len(listseq)-1)
print(listseq, "pop(len(list) -1 ")
print('')