def bin1(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            high = mid - 1
        elif x > arr[mid]:
            low = mid + 1
    else:
        return 1


arr1 = [2, 3, 9, 5, 4, 3, 5, 6, 7, 10]
y = int(input("Enter the number: "))
a = bin1(arr1, y)
if a >= 0:
    print(y, "is at index:", a)
else:
    print("The number is not there!!!")
