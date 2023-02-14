lst = []
r = int(input("How many rows? "))
c = int(input("How many columns? "))
for i in range(r):
    row = []
    print(row)
    for j in range(c):
        elem = int(input("Element" + str(i) + str(j) + ":"))
        row.append(elem)
    lst.append(row)
print("List created is:", lst)

