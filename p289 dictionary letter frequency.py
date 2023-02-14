n = input("Enter the name: ").strip().lower()
c = 0
dic1 = {}
for i in n:
    print(i, end="")
    if i not in dic1:
        dic1[i] = 0
print("")
for j in n:
    if j in dic1:
        dic1[j] += 1
    else:
        dic1[j] = 1
print("The counter of the dictionary is....")
print(dic1)
for k, v in dic1.items():
    print(k, "-", v)
