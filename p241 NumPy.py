import numpy as np

list1 = []
n = int(input("Enter the limit: "))
for i in range(1, n + 1):
    x = int(input("Enter the values: "))
    list1.append(x)
print(list1)
arr = np.array(list1)
print(arr)
for i in range(len(arr)):
    print(arr[i])
