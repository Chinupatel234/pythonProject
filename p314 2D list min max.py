lst = []
rows = int(input("Enter the rows: "))
columns = int(input("Enter the columns: "))
for i in range(rows):
    row = []
    for j in range(columns):
        n = int(input("Element" + str(i) + str(j) + ":"))
        row.append(n)
    lst.append(row)


print(lst)
lst1 = []
s = 0
for j in lst:
    lst1.append(sum(j))
    s = s + sum(j)
print("Minimum rums in an over:", min(lst1))
print("Maximum rums in an over:", max(lst1))
print("Total runs:", s)



