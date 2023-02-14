n = input("Enter the string: ")
list1 = []

for i in n:
    print(i, end="")
    list1.append(i)

print("")
print(list1)

m = input("Enter the letter which you want to search for:")
for j in range(len(list1)):
    if m in list1[j]:
        print(m, "is at index", j)

