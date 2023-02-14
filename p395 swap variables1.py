a = int(input("Enter the number1: "))
b = int(input("Enter the number2: "))

print(f"Before swap: a = {a} b = {b}")

temp = a  # temp will get the value of a
a = b  # a will get the value of b
b = temp  # b will get the value of temp

print(f"After swap: a = {a} b = {b}")
