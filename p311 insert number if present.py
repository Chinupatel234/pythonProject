def insert(arr, num):
    if num in arr:
        arr.append(num)
        return "number exists and added"
    return "number not present"


arr1 = [1, 2, 3, 4, 5]
n = int(input("Enter the number: "))
result = insert(arr1, n)
print(result)
print(arr1)
