def insertq(arr):
    data = int(input("Enter the value to be inserted: "))
    arr.append(data)
    deleteq(arr)


def deleteq(arr):
    if arr == []:
        print("Queue is empty...")
    else:
        print("Deleted element is:", arr[0])
        del arr[0]


arr = [1, 2, 3, 4, 5, 6]
insertq(arr)
print(arr)
