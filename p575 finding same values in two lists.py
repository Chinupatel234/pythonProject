lst1 = [5, 6, 4, 2, 7, 9, 8]
lst2 = [6, 7, 8, 9, 42, 4, 5]
lst3 = []
dic1 = {}
for i in lst1:
    if i not in dic1:
        dic1[i] = 1
    else:
        dic1[i] += 1
print(dic1)
for j in lst2:
    if j in dic1 and j > 0:
        lst3.append(j)
    else:
        pass
print(lst3)
# # lst1.sort()
# # lst2.sort()
# a = set(lst1)
# b = set(lst2)
# print(a)
# print(b)
# c = a.intersection(b)
# print(c)
