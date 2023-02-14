n = int(input("Enter the limit: "))
for i in range(n):
    for j in range(i + 1):
        if j == 0 or j == i:
            print("1", end=" ")
        else:
            print("2", end=" ")
    print("")
