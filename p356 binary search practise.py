def bin_search(lst3, k1):
    low = 0
    high = len(lst3) - 1
    while low <= high:
        mid = (low + high) // 2
        if k1 == lst3[mid]:
            return mid
        elif k1 < lst3[mid]:
            high = mid - 1
        else:
            low = mid + 1
    else:
        return -1


lst2 = [1, 2, 3, 4, 5, 6]
k = int(input("Enter the number you want to search: "))
c = bin_search(lst2, k)
if c >= 0:
    print("Number found at index", c, "and position", str(c + 1))
else:
    print("Sorry...number not found...")
