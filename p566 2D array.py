n = int(input("Enter how many rows: "))
k = int(input("Enter how many columns: "))
lst1 = []
for i in range(n):
    lst2 = []
    for j in range(k):
        m = int(input("Enter your height" + str(i) + str(j) + ":"))
        b = int(input("Enter you weight" + str(i) + str(j) + ":"))
        c = [m, b]
        lst2.append(c)
    lst1.append(lst2)
print("")
for i in range(len(lst1)):
    for j in range(len(lst1)):
        print(lst1[i][j], end="")
    print("")
