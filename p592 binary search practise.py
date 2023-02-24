def binary(lst2, key1):
    low = 0
    high = len(lst2) - 1
    while low <= high:
        mid = (low + high) // 2
        if key1 == lst2[mid]:
            return mid
        elif key1 <= lst2[mid]:
            high = mid - 1
        else:
            low = mid + 1
    else:
        return -1


lst1 = [11, 22, 33, 44, 55]
print(lst1)
key = int(input("Enter the number that you want it search: "))
a = binary(lst1, key)
if a >= 0:
    print(f"Number found at index: {a} and position: {a + 1}")
else:
    print("Sorry...number not found!!!")
