arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(arr1)):
    for j in range(len(arr1)):
        print(arr1[i][j], end=" ")
    print("")
arr1[2][1] = 69
print("")
for i in range(len(arr1)):
    for j in range(len(arr1)):
        print(arr1[i][j], end=" ")
    print("")
print("")

