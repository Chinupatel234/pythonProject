lst1 = [1, 2, 3, 4, 5, 6]
c = 0
n = int(input("Enter the index you want to search for: "))
for i in range(len(lst1)):
    if n == i:
        c += 1
        temp = lst1[i + 1]
        lst1[i + 1] = lst1[i + 2]
        lst1[i + 2] = temp
    print(lst1[i], end=" ")

if c == 0:
    print("Sorry...index not found!!!")
