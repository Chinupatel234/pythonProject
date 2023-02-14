def duplicate(arr1, num):
    if arr1.count(num) > 1:
        arr1.remove(num)
        return "Duplicate number has been deleted"
    return "Number present only once"


arr = [3, 2, 45, 6, 3, 6, 7, 7, 10]
print(arr)
n = int(input("Enter the number: "))
result = duplicate(arr, n)
print(result)
print(arr)
