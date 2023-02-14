lst = []
rows = int(input("Enter the rows: "))
columns = int(input("Enter the columns: "))
for i in range(rows):
    row = []
    for j in range(columns):
        n = int(input("Element" + str(i) + str(j) + ":"))
        row.append(n)
    lst.append(row)
print("")
print(lst)
transpose = zip(*lst)
for i in transpose:
    print(i)
