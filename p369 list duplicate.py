lst = [2, 3, 1, 3, 4, 3, 3, 4, 6, 6, 8, 9]
lst1 = []
for i in lst:
    if i not in lst1:
        lst1.append(i)
    else:
        continue
print("Original list:", lst)
print("New list:", lst1)
