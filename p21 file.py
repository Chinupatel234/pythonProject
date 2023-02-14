file = open("d:\\chinmay.txt", "w")
list1 = []
for i in range(5):
    name = input("Enter the name: ")
    list1.append(name + "\n")
file.writelines(list1)
file.close()
