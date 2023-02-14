n = int(input("Enter the limit:"))
list1 = [None] * n
for i in range(n):
    list1[i] = int(input("Enter the number" + str(i + 1) + ":"))
print(list1)
    