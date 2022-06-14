print("Practice 2. Data processing")
print("Strings format")
print('')

print("----- Task 02 -----")
a = 1/3
print("{:7.3f}".format(a))
print('')

print("----- Task 03 -----")
a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))
print('')

print("----- Task 04 -----")
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " + " + n2 + " = ", "{:7.3f} {:7.3f} {:7.3f}".format(float(n1), float(n2), float(n3)))
