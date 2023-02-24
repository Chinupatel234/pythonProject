from array import *

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr1 = array("i", lst1)
print("Initial array: ")
for i in arr1:
    print(i, end=" ")
print("")
a = arr1[-1: -3: -1]
print(a)
print("")
b = arr1[::-1]
print(b)
print("")
c = arr1[::2]
print(c)
