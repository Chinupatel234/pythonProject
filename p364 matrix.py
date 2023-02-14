lst1 = []
r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))
for i in range(r):
    row = []
    for j in range(c):
        m = int(input("Enter the number" + str(i) + str(j) + ":"))
        row.append(m)
    lst1.append(row)
print(lst1)
for k in range(len(lst1)):
    for c in range(len(lst1)):
        print(lst1[k][c], end=" ")
    print("")
