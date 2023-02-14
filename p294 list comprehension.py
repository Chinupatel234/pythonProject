# list1 = []
# for i in range(1, 6):
# list1.append(i * 2)
# print(list1)

list1 = [i * 2 for i in range(1, 6)]
print(list1)


# list2 = []
# for i in range(1, 50):
#    if i % 7 == 0:
#        list2.append(i)
# print(list2)

list2 = [i for i in range(1, 50) if i % 7 == 0]
print(list2)


# list3 = []
# for i in range(2, 10):
#    if i < 5:
#        print(i, end=" ")
#    else:
#        print(i * 2, end=" ")
#    list3.append(i)

# print("")

list3 = [(num if num < 5 else num * 2) for num in range(2, 10)]
print(list3)
