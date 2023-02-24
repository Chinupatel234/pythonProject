import array as arr

a = arr.array("i", [1, 2, 3, 4, 5])
b = arr.array("d", [1.2, 2, 3.5, 4, 5])
for i in range(0, len(a)):
    print(a[i], end=" ")
print("")
for i in range(0, len(b)):
    print(b[i], end=" ")
