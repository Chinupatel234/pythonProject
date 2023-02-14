lst = [22, 33, 44, 55, 66, 77, 88]
n = int(input("Enter the slice1: "))
m = int(input("Enter the slice2: "))
for i in range(n, m):
    print(lst[i], end=",")
    