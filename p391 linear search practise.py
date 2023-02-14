lst = []
n = int(input("Enter the limit: "))
for i in range(n):
    m = int(input("Enter the number" + str(i + 1) + ":"))
    lst.append(m)
print("")
print(lst)
num = int(input("Enter the number you want to search for: "))
s = 0
for i in range(0, len(lst)):
    if num == lst[i]:
        s += 1
        print("The number found at position " + str(i + 1))
if s == 0:
    print("Sorry...the number not found!!!")

