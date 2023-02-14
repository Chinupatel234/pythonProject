n = input("Enter the name: ")
a = n.split()
print(a)
for j in a:
    x = j[0].capitalize() + j[1:len(j) - 1] + j[-1].capitalize()
    print(x, end=" ")
