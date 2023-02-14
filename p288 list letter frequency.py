n = input("Enter the name: ").strip().lower()
list1 = []
for i in n:
    print(i, end="")
    list1.append(i)

print("")
print(list1)
for i in range(len(list1)):
    a = list1.count(list1[i])
    print(list1[i], "-", a)

