print("Practice 2. Data processing")
print("Digits")
print('')

print("----- Task 01 -----")
a = int(16)
b = int(8)
c = int(a/b)
print("Devisin 16 and 8")
print(c)

d = int(b/a)
print("Devisin 8 and 16")
print(d)

e = int(b%a)
print("The remainder from devision of digits 8 and 16")
print(e)

f = int(a%b)
print("The remainder from devision of digits 16 and 8")
print(f)

g = int(a ** b)
print("Exponentiation into 8 of digit 16")
print(g)
print('')

print("----- Task 03 -----")
#param = "string" + 15 Error
#Solution - conversion into string
param = "string" + str(15)
print(param)
print('')

print("----- Task 04 -----")
print("Sum of input digits")
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " + " + n2 + " = ", n3)
