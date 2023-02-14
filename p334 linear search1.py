def linear_search(a1, n1):
    k = 0
    for j in range(len(a1)):
        if a1[j] == n1:
            k = 1
            pos = j + 1
            print("Number found at", pos, "position")
            break
    if k == 0:
        print("Number not found...")


a = []
size = int(input("Enter the size: "))
for i in range(size):
    n = int(input("Enter the element" + str(i + 1) + ":"))
    a.append(n)
m = int(input("Enter the item which you want to search: "))
linear_search(a, m)
