def l_search(arr1, item1):
    i = 0
    while i < len(arr1) and arr1[i] != item1:
        i += 1
    if i < len(arr1):
        return i
    else:
        return False


n = int(input("Enter the desired linear list size(max50)..."))
print("Enter the elements for linear list")
arr1 = [0]*n

for i in range(n):
    arr1[i] = int(input("Element" + str(i) + ":"))
item1 = int(input("Enter the element to be searched for..."))
index = l_search(arr1, item1)

if index:
    print("Element found at index:", index, "position:", (index + 1))
else:
    print("Sorry!element not found...")
