a = "12345"
m = int(input("Enter the shift: "))
b = a.split()
for i in b:
    print(i, end="")
print("")
for i in b:
    c = i[m:]
    d = i[:m]
    print(c + d, end="")
